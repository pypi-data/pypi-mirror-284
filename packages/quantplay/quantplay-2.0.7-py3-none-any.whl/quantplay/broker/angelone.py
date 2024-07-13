import json
import traceback
from typing import Callable, Dict

import polars as pl
import pyotp
import copy
from retrying import retry
from SmartApi import SmartConnect

from quantplay.exception.exceptions import TokenException as QuantplayTokenException
import binascii
from quantplay.broker.generics.broker import Broker
from quantplay.exception.exceptions import InvalidArgumentException
from quantplay.model.broker.generics import ModifyOrderRequest, UserBrokerProfileResponse
from quantplay.utils.exchange import Market as MarketConstants
from quantplay.exception.exceptions import (
    QuantplayOrderPlacementException,
    TokenException,
    ServiceException,
    RetryableException,
    retry_exception,
    BrokerException,
)
from requests.exceptions import ConnectTimeout, ConnectionError
import pickle
import codecs
from quantplay.wrapper.aws.s3 import S3Utils

from quantplay.utils.pickle_utils import InstrumentData

from quantplay.utils.constant import Constants, OrderType, timeit


class AngelOne(Broker):
    order_sl = "STOPLOSS_LIMIT"
    order_slm = "STOPLOSS_MARKET"

    @timeit(MetricName="Angelone:init")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=5,
        retry_on_exception=retry_exception,
    )
    def __init__(
        self,
        order_updates=None,
        api_key=None,
        user_id=None,
        mpin=None,
        totp: str | None = None,
        refresh_token=None,
        feed_token=None,
        access_token=None,
        load_instrument=True,
    ):
        super(AngelOne, self).__init__()
        self.order_updates = order_updates

        try:
            if refresh_token:
                self.wrapper = SmartConnect(
                    api_key=api_key,
                    access_token=access_token,
                    refresh_token=refresh_token,
                    feed_token=feed_token,
                )
                self.refresh_token = refresh_token
            else:
                if totp is None:
                    raise InvalidArgumentException("TOTP Key is Missing")
                self.wrapper = SmartConnect(api_key=api_key)
                response = self.invoke_angelone_api(
                    self.wrapper.generateSession,
                    clientCode=user_id,
                    password=mpin,
                    totp=pyotp.TOTP(totp).now(),
                )
                if response["status"] is False:
                    if "message" in response:
                        raise InvalidArgumentException(response["message"])
                    raise InvalidArgumentException("Invalid API credentials")
                token_data = self.invoke_angelone_api(
                    self.wrapper.generateToken, refresh_token=self.wrapper.refresh_token
                )
                self.refresh_token = token_data["data"]["refreshToken"]
        except InvalidArgumentException:
            raise
        except binascii.Error:
            raise InvalidArgumentException("Invalid TOTP key provided")
        except Exception as e:
            print(e)
            raise RetryableException(str(e))

        self.user_id = user_id
        self.api_key = self.wrapper.api_key

        if load_instrument:
            self.load_instrument()

    def set_wrapper(self, serialized_wrapper):
        self.wrapper: SmartConnect = pickle.loads(
            codecs.decode(serialized_wrapper.encode(), "base64")
        )

    def handle_exception(self, response):
        if "errorCode" in response and response["errorCode"] == "AG8001":
            raise TokenException(f"{self.user_id}: Invalid Token")

    @timeit(MetricName="Angelone:load_instrument")
    def load_instrument(self, file_name: str | None = None) -> None:
        try:
            instrument_data_instance = InstrumentData.get_instance()
            if instrument_data_instance is not None:
                self.symbol_data = instrument_data_instance.load_data(
                    "angelone_instruments"
                )
            Constants.logger.info("[LOADING_INSTRUMENTS] loading data from cache")
        except Exception:
            self.instrument_data = S3Utils.read_csv(
                "quantplay-market-data",
                "symbol_data/angelone_instruments.csv",
                read_from_local=False,
            )
            self.initialize_symbol_data(save_as="angelone_instruments")

        self.initialize_broker_symbol_map()

    def get_symbol(self, symbol, exchange=None):
        if exchange == "NSE":
            if symbol in ["NIFTY", "BANKNIFTY"]:
                return symbol
            if "-EQ" not in symbol:
                return f"{symbol}-EQ"
            else:
                return symbol
        if exchange == "BSE":
            return symbol

        if symbol not in self.quantplay_symbol_map:
            return symbol
        return self.quantplay_symbol_map[symbol]

    def get_order_type(self, order_type):
        if order_type == OrderType.sl:
            return AngelOne.order_sl
        elif order_type == OrderType.slm:
            return AngelOne.order_slm

        return order_type

    def get_product(self, product):
        if product == "NRML":
            return "CARRYFORWARD"
        elif product == "CNC":
            return "DELIVERY"
        elif product == "MIS":
            return "INTRADAY"
        elif product in ["BO", "MARGIN", "INTRADAY", "CARRYFORWARD", "DELIVERY"]:
            return product

        raise InvalidArgumentException(
            "Product {} not supported for trading".format(product)
        )

    @timeit(MetricName="Angelone:get_ltp")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
    )
    def get_ltp(self, exchange=None, tradingsymbol=None) -> float:
        if tradingsymbol in MarketConstants.INDEX_SYMBOL_TO_DERIVATIVE_SYMBOL_MAP:
            tradingsymbol = MarketConstants.INDEX_SYMBOL_TO_DERIVATIVE_SYMBOL_MAP[
                tradingsymbol
            ]

        symbol_data = self.symbol_data[
            f"{exchange}:{self.get_symbol(tradingsymbol, exchange=exchange)}"
        ]
        symboltoken = symbol_data["token"]

        response = self.invoke_angelone_api(
            self.wrapper.ltpData,
            exchange=exchange,
            tradingsymbol=tradingsymbol,
            symboltoken=symboltoken,
        )

        if "status" in response and response["status"] is False:
            raise InvalidArgumentException(
                "Failed to fetch ltp broker error {}".format(response)
            )

        return response["data"]["ltp"]

    @timeit(MetricName="Angelone:place_order")
    def place_order(
        self,
        tradingsymbol=None,
        exchange=None,
        quantity=None,
        order_type=None,
        transaction_type=None,
        tag=None,
        product=None,
        price=None,
        trigger_price=None,
    ):
        order = {}
        try:
            if trigger_price == 0:
                trigger_price = None

            order_type = self.get_order_type(order_type)
            product = self.get_product(product)
            tradingsymbol = self.get_symbol(tradingsymbol, exchange=exchange)

            variety = "NORMAL"
            if order_type in [AngelOne.order_sl, AngelOne.order_slm]:
                variety = "STOPLOSS"

            symbol_data = self.symbol_data[f"{exchange}:{self.get_symbol(tradingsymbol)}"]
            symbol_token = symbol_data["token"]

            order = {
                "transactiontype": transaction_type,
                "variety": variety,
                "tradingsymbol": tradingsymbol,
                "ordertype": order_type,
                "triggerprice": trigger_price,
                "exchange": exchange,
                "symboltoken": symbol_token,
                "producttype": product,
                "price": price,
                "quantity": quantity,
                "duration": "DAY",
                "ordertag": tag,
            }

            Constants.logger.info("[PLACING_ORDER] {}".format(json.dumps(order)))
            return self.invoke_angelone_api(self.wrapper.placeOrder, orderparams=order)

        except (TimeoutError, ConnectTimeout):
            Constants.logger.info(f"[ANGELONE_REQUEST_TIMEOUT] {order}")

        except Exception as e:
            traceback.print_exc()
            Constants.logger.error(f"[PLACE_ORDER_FAILED] {e} {order}")
            raise QuantplayOrderPlacementException(str(e))

    def get_variety(self, variety):
        if variety == "regular":
            return "NORMAL"
        return variety

    @timeit(MetricName="Angelone:modify_order")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
    )
    def modify_order(self, order_to_modify: ModifyOrderRequest) -> str:
        data = copy.deepcopy(order_to_modify)
        order_id = str(data["order_id"])
        try:
            orders = self.orders()
            filtered_order = orders.filter(pl.col("order_id") == str(data["order_id"]))
            order = filtered_order.to_dicts()[0]
            quantity = order["quantity"]
            token = order["token"]
            exchange = order["exchange"]
            product = self.get_product(order["product"])
            variety = order["variety"]
            order_type = self.get_order_type(data["order_type"])

            if "trigger_price" not in data:
                data["trigger_price"] = None

            if "quantity" in data and int(data["quantity"]) > 0:
                quantity = data["quantity"]

            order_id = data["order_id"]

            order_params = {
                "orderid": order_id,
                "variety": variety,
                "price": data["price"],
                "triggerprice": data["trigger_price"],
                "producttype": product,
                "duration": "DAY",
                "quantity": quantity,
                "symboltoken": token,
                "ordertype": order_type,
                "exchange": exchange,
                "tradingsymbol": self.get_symbol(
                    order["tradingsymbol"], exchange=exchange
                ),
            }

            Constants.logger.info(f"Modifying order [{order_id}] params [{order_params}]")
            response = self.invoke_angelone_api(
                self.wrapper.modifyOrder, orderparams=order_params
            )
            Constants.logger.info(f"[MODIFY_ORDER_RESPONSE] {response}")
            return order_id
        except Exception as e:
            traceback.print_exc()
            Constants.logger.error(
                f"[MODIFY_ORDER_FAILED] for {data['order_id']} failed with exception {e}"
            )
            raise

    @timeit(MetricName="Angelone:cancel_order")
    def cancel_order(self, order_id, variety="NORMAL"):
        self.wrapper.cancelOrder(order_id=order_id, variety=variety)

    @timeit(MetricName="Angelone:holdings")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=15000,
        stop_max_attempt_number=5,
        retry_on_exception=retry_exception,
    )
    def holdings(self):
        try:
            holdings = self.invoke_angelone_api(self.wrapper.holding)
        except Exception:
            raise RetryableException("Access Denied retrying")
        self.handle_exception(holdings)

        if holdings["data"] is None or len(holdings["data"]) == 0:
            return pl.DataFrame(schema=self.holidings_schema)

        holdings = pl.from_dicts(holdings["data"])
        holdings = holdings.rename(
            {
                "averageprice": "average_price",
                "ltp": "price",
                "symboltoken": "token",
            }
        )

        holdings = holdings.with_columns(
            pl.lit(0).alias("pledged_quantity"),
            pl.col("tradingsymbol").str.replace("-EQ", "").alias("tradingsymbol"),
            (pl.col("quantity").mul(pl.col("average_price"))).alias("buy_value"),
            (pl.col("quantity").mul(pl.col("price"))).alias("current_value"),
            (((pl.col("price") / (pl.col("average_price"))).sub(1)).mul(100)).alias(
                "pct_change"
            ),
        )

        return holdings

    @timeit(MetricName="Angelone:positions")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=15000,
        stop_max_attempt_number=5,
        retry_on_exception=retry_exception,
    )
    def positions(self, drop_cnc: bool = True):
        try:
            positions = self.invoke_angelone_api(self.wrapper.position)
        except Exception:
            raise RetryableException("Access Denied retrying")
        self.handle_exception(positions)

        if positions["data"] is None:
            return pl.DataFrame(schema=self.positions_schema)

        positions_df = pl.from_dicts(positions["data"])

        if "optiontype" not in positions_df.columns:
            positions_df = positions_df.with_columns(pl.lit(None).alias("optiontype"))

        positions_df = positions_df.rename(
            {
                "optiontype": "option_type",
                "sellqty": "sell_quantity",
                "buyqty": "buy_quantity",
                "totalsellvalue": "sell_value",
                "totalbuyvalue": "buy_value",
                "producttype": "product",
                "symboltoken": "token",
            },
        )

        positions_df = positions_df.with_columns(
            (
                pl.col("buy_quantity").cast(pl.Int32) + pl.col("cfbuyqty").cast(pl.Int32)
            ).alias("buy_quantity")
        )
        positions_df = positions_df.with_columns(
            (
                pl.col("sell_quantity").cast(pl.Int64)
                + pl.col("cfsellqty").cast(pl.Int64)
            ).alias("sell_quantity")
        )
        positions_df = positions_df.with_columns(
            pl.col("pnl").cast(pl.Float64).alias("pnl"),
            pl.col("ltp").cast(pl.Float64).alias("ltp"),
            (pl.col("buy_quantity") - pl.col("sell_quantity")).alias("quantity"),
        )

        positions_df = positions_df.with_columns(
            pl.when(pl.col("product") == "DELIVERY")
            .then(pl.lit("CNC"))
            .when(pl.col("product") == "CARRYFORWARD")
            .then(pl.lit("NRML"))
            .when(pl.col("product") == "INTRADAY")
            .then(pl.lit("MIS"))
            .otherwise(pl.col("product"))
            .alias("product")
        )

        positions_df = positions_df.with_columns(
            (
                (
                    pl.col("buy_value").cast(pl.Float64)
                    - pl.col("sell_value").cast(pl.Float64)
                )
                / pl.col("quantity").cast(pl.Int32)
            ).alias("average_price")
        )
        positions_df = positions_df.with_columns(
            pl.when(pl.col("quantity") == 0)
            .then(pl.lit(0))
            .otherwise(pl.col("average_price"))
            .alias("average_price")
        )
        return positions_df[list(self.positions_schema.keys())].cast(
            self.positions_schema
        )

    @timeit(MetricName="Angelone:orders")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
        retry_on_exception=retry_exception,
    )
    def orders(self, tag: str | None = None, add_ltp: bool = True) -> pl.DataFrame:
        try:
            order_book = self.invoke_angelone_api(self.wrapper.orderBook)
        except Exception:
            raise RetryableException("Access Denied retrying")
        self.handle_exception(order_book)

        if order_book["data"]:
            orders_df = pl.DataFrame(order_book["data"])

            if len(orders_df) == 0:
                return pl.DataFrame(schema=self.orders_schema)

            if add_ltp:
                positions = self.positions()
                positions = positions.sort("product").group_by("tradingsymbol").head(1)

                if "ltp" in orders_df:
                    orders_df = orders_df.drop(["ltp"])
                orders_df = orders_df.join(
                    positions.select(["tradingsymbol", "ltp"]),
                    on="tradingsymbol",
                    how="left",
                )
            else:
                orders_df = orders_df.with_columns(pl.lit(None).alias("ltp"))

            orders_df = orders_df.rename(
                {
                    "orderid": "order_id",
                    "ordertag": "tag",
                    "averageprice": "average_price",
                    "producttype": "product",
                    "transactiontype": "transaction_type",
                    "triggerprice": "trigger_price",
                    "price": "price",
                    "filledshares": "filled_quantity",
                    "unfilledshares": "pending_quantity",
                    "updatetime": "order_timestamp",
                    "ordertype": "order_type",
                    "symboltoken": "token",
                }
            )

            orders_df = orders_df.with_columns(
                pl.col("order_timestamp")
                .str.to_datetime("%d-%b-%Y %H:%M:%S")
                .alias("order_timestamp")
            )
            orders_df = orders_df.with_columns(
                pl.col("order_timestamp").alias("update_timestamp")
            )

            if tag:
                orders_df = orders_df.filter(pl.col("tag") == tag)

            orders_df = orders_df.with_columns(
                pl.when(pl.col("status") == "open")
                .then(pl.lit("OPEN"))
                .when(pl.col("status") == "cancelled")
                .then(pl.lit("CANCELLED"))
                .when(pl.col("status") == "trigger pending")
                .then(pl.lit("TRIGGER PENDING"))
                .when(pl.col("status") == "complete")
                .then(pl.lit("COMPLETE"))
                .when(pl.col("status") == "rejected")
                .then(pl.lit("REJECTED"))
                .otherwise(pl.col("status"))
                .alias("status"),
                pl.when(pl.col("product") == "DELIVERY")
                .then(pl.lit("CNC"))
                .when(pl.col("product") == "CARRYFORWARD")
                .then(pl.lit("NRML"))
                .when(pl.col("product") == "INTRADAY")
                .then(pl.lit("MIS"))
                .otherwise(pl.col("product"))
                .alias("product"),
                pl.when(pl.col("order_type") == AngelOne.order_sl)
                .then(pl.lit(OrderType.sl))
                .when(pl.col("order_type") == AngelOne.order_slm)
                .then(pl.lit(OrderType.slm))
                .otherwise(pl.col("order_type"))
                .alias("order_type"),
                pl.lit(self.user_id).alias("user_id"),
                pl.lit("").alias("status_message"),
                pl.lit("").alias("status_message_raw"),
            )

            return orders_df[list(self.orders_schema.keys())].cast(self.orders_schema)
        else:
            if "message" in order_book and order_book["message"] == "SUCCESS":
                return pl.DataFrame(schema=self.orders_schema)

            if "errorcode" in order_book and order_book["errorcode"] == "AB1010":
                raise TokenException("Can't Fetch order book because session got expired")

            else:
                Constants.logger.error(order_book)
                traceback.print_exc()
                raise ServiceException("Unknown error while fetching order book [{}]")

    @timeit(MetricName="Angelone:profile")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
        retry_on_exception=retry_exception,
    )
    def profile(self):
        try:
            profile_data = self.invoke_angelone_api(
                self.wrapper.getProfile, refresh_token=self.refresh_token
            )
        except Exception:
            raise RetryableException("Access Denied retrying")

        self.handle_exception(profile_data)

        profile_data = profile_data["data"]
        response: UserBrokerProfileResponse = {
            "user_id": profile_data["clientcode"],
            "full_name": profile_data["name"],
            "email": profile_data["email"],
        }

        return response

    @timeit(MetricName="Angelone:margins")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
        retry_on_exception=retry_exception,
    )
    def margins(self):
        api_margins = self.invoke_angelone_api(self.wrapper.rmsLimit)
        self.handle_exception(api_margins)

        if "data" in api_margins and api_margins["data"] is None:
            if "errorcode" in api_margins and api_margins["errorcode"] == "AB1004":
                raise TokenException("Angelone server not not responding")

            return {"margin_used": 0, "margin_available": 0, "total_balance": 0}

        api_margins = api_margins["data"]

        try:
            margins = {
                "margin_used": float(api_margins["net"]),
                "margin_available": float(api_margins["net"]),
                "total_balance": float(api_margins["net"]),
            }

            return margins

        except (ConnectionError, ConnectTimeout):
            raise BrokerException("Angelone broker error while fetching margins")

        except Exception as e:
            raise RetryableException(f"Angelone: Failed to fetch margin {e}")

    def account_summary(self):
        pnl = 0

        margins = self.margins()
        positions = self.positions()

        if len(positions) > 0:
            pnl = positions["pnl"].sum()

        response = {
            "margin_used": margins["margin_used"],
            "total_balance": margins["total_balance"],
            "margin_available": margins["margin_available"],
            "pnl": pnl,
        }

        return response

    def invoke_angelone_api(self, fn: Callable, *args, **kwargs) -> Dict:
        try:
            response = fn(*args, **kwargs)
            if isinstance(response, bytes):
                raise InvalidArgumentException(
                    "Invalid data response. AngelOne sent incorrect data, Please check."
                )

            return response

        except TokenException:
            raise QuantplayTokenException("Token Expired")

        except Exception:
            traceback.print_exc()
            raise RetryableException("Failed to fetch user profile")
