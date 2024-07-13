import copy
import hashlib
import requests
import json
import time
import pandas as pd
import polars as pl

from quantplay.model.broker.generics import ModifyOrderRequest, UserBrokerProfileResponse
from quantplay.utils.constant import Constants, timeit, OrderType
from quantplay.broker.generics.broker import Broker
from quantplay.exception.exceptions import InvalidArgumentException
import pyotp
import _thread as thread
import binascii
from quantplay.utils.pickle_utils import InstrumentData
from quantplay.exception.exceptions import (
    QuantplayOrderPlacementException,
    retry_exception,
    RetryableException,
)
from retrying import retry
from quantplay.wrapper.aws.s3 import S3Utils


class Motilal(Broker):
    user_id = "motilal_user_id"
    api_key = "motilal_api_key"
    password = "motilal_password"
    auth_token = "motilal_auth_token"
    two_factor_authentication = "motilal_2FA"
    secret_key = "motilal_secret_key"

    headers = {
        "Accept": "application/json",
        "User-Agent": "MOSL/V.1.1.0",
        "SourceId": "WEB",
        "MacAddress": "00:50:56:BD:F4:0B",
        "ClientLocalIp": "192.168.165.165",
        "ClientPublicIp": "106.193.137.95",
        "osname": "Ubuntu",
        "osversion": "10.0.19041",
        "devicemodel": "AHV",
        "manufacturer": "DELL",
        "productname": "Your Product Name",
        "productversion": "Your Product Version",
        "installedappid": "AppID",
        "browsername": "Chrome",
        "browserversion": "105.0",
    }

    @timeit(MetricName="Motilal:__init__")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=2,
        retry_on_exception=retry_exception,
    )
    def __init__(
        self,
        is_uat=False,
        headers=None,
        load_instrument=True,
        user_id=None,
        password=None,
        api_key=None,
        two_fa=None,
        totp=None,
        order_updates=None,
    ):
        super(Motilal, self).__init__()
        self.order_updates = order_updates

        self.instrument_data_by_exchange = {}

        uat = ""
        if is_uat:
            uat = "uat"

        self.url = (
            "https://{}openapi.motilaloswal.com/rest/login/v3/authdirectapi".format(uat)
        )
        self.otp_url = (
            "https://{}openapi.motilaloswal.com/rest/login/v3/resendotp".format(uat)
        )
        self.verify_otp_url = (
            "https://{}openapi.motilaloswal.com/rest/login/v3/verifyotp".format(uat)
        )
        self.ltp_utl = (
            "https://{}openapi.motilaloswal.com/rest/report/v1/getltpdata".format(uat)
        )
        self.place_order_url = (
            "https://{}openapi.motilaloswal.com/rest/trans/v1/placeorder".format(uat)
        )
        self.get_profile_url = (
            "https://{}openapi.motilaloswal.com/rest/login/v1/getprofile".format(uat)
        )
        self.margin_summary_url = "https://{}openapi.motilaloswal.com/rest/report/v1/getreportmarginsummary".format(
            uat
        )
        self.modify_order_url = (
            "https://{}openapi.motilaloswal.com/rest/trans/v2/modifyorder".format(uat)
        )
        self.order_book_url = (
            "https://{}openapi.motilaloswal.com/rest/book/v1/getorderbook".format(uat)
        )
        self.cancel_order_url = (
            "https://{}openapi.motilaloswal.com/rest/trans/v1/cancelorder".format(uat)
        )
        self.positions_url = (
            "https://{}openapi.motilaloswal.com/rest/book/v1/getposition".format(uat)
        )
        self.holdings_url = (
            "https://{}openapi.motilaloswal.com/rest/report/v1/getdpholding".format(uat)
        )
        self.order_details_url = "https://{}openapi.motilaloswal.com/rest/book/v2/getorderdetailbyuniqueorderid".format(
            uat
        )

        try:
            if headers:
                self.headers = headers
            else:
                self.generate_token(user_id, password, api_key, two_fa, totp)
            profile = self.profile()
            self.user_id = profile["user_id"]
        except binascii.Error:
            raise InvalidArgumentException("Invalid TOTP key provided")
        except InvalidArgumentException:
            raise
        except Exception as e:
            raise RetryableException(str(e))

        if load_instrument:
            self.load_instrument()

        self.order_type_sl = "STOPLOSS"
        self.nfo_exchange = "NSEFO"
        self.exchange_code_map = {"NFO": "NSEFO", "CDS": "NSECD", "BFO": "BSEFO"}

    @timeit(MetricName="Motilal:load_file_by_url")
    def load_file_by_url(self, exchange):
        data_url = "https://openapi.motilaloswal.com/getscripmastercsv?name={}".format(
            exchange
        )
        df = pd.read_csv(data_url)
        self.instrument_data_by_exchange[exchange] = df

    @timeit(MetricName="Motilal:load_instrument")
    def load_instrument(self, file_name: str | None = None) -> None:
        try:
            self.symbol_data = InstrumentData.get_instance().load_data(  # type: ignore
                "motilal_instruments"
            )
            Constants.logger.info("[LOADING_INSTRUMENTS] loading data from cache")
        except Exception:
            self.instrument_data = S3Utils.read_csv(
                "quantplay-market-data",
                "symbol_data/motilal_instruments.csv",
                read_from_local=False,
            )
            self.initialize_symbol_data(save_as="motilal_instruments")

        self.initialize_broker_symbol_map()

    def get_symbol(self, symbol, exchange=None):
        if symbol not in self.quantplay_symbol_map:
            return symbol
        return self.quantplay_symbol_map[symbol]

    def get_order_type(self, order_type):
        if order_type == OrderType.sl:
            return "STOPLOSS"
        return order_type

    def get_exchange(self, exchange):
        if exchange in self.exchange_code_map:
            return self.exchange_code_map[exchange]

        return exchange

    def get_product(self, product):
        if product == "CNC":
            return "DELIVERY"
        elif product == "NRML":
            return "NORMAL"
        elif product == "DELIVERY":
            return "DELIVERY"
        return "NORMAL"

    def place_order_quantity(self, quantity, tradingsymbol, exchange):
        lot_size = self.get_lot_size(exchange, tradingsymbol)
        quantity_in_lots = int(quantity / lot_size)

        return quantity_in_lots

    def get_lot_size(self, exchange, tradingsymbol):
        tradingsymbol = self.get_symbol(tradingsymbol, exchange=exchange)
        if exchange == "NSEFO":
            exchange = "NFO"
        elif exchange == "BSEFO":
            exchange = "BFO"
        try:
            return int(
                self.symbol_data["{}:{}".format(exchange, tradingsymbol)]["lot_size"]
            )
        except Exception as e:
            Constants.logger.error(
                "[GET_LOT_SIZE] unable to get lot size for {} {}".format(
                    exchange, tradingsymbol
                )
            )
            raise e

    def generate_token(self, user_id, password, api_key, two_fa, totp):
        current_totp = pyotp.TOTP(totp).now()
        Constants.logger.info("TOTP is {}".format(current_totp))
        # initializing string
        str = "{}{}".format(password, api_key)
        result = hashlib.sha256(str.encode())

        data = {
            "userid": user_id,
            "password": result.hexdigest(),
            "2FA": two_fa,
            "totp": current_totp,
        }

        self.headers["ApiKey"] = api_key
        self.headers["vendorinfo"] = user_id
        response = requests.post(self.url, headers=self.headers, data=json.dumps(data))

        resp_json = response.json()
        if "status" in resp_json and resp_json["status"] == "ERROR":
            raise InvalidArgumentException(resp_json["message"])
        Constants.logger.info("login response {}".format(resp_json))
        self.headers["Authorization"] = resp_json["AuthToken"]
        self.user_id = user_id

    def send_otp(self):
        response = requests.post(self.otp_url, headers=self.headers).json()
        Constants.logger.info(response)
        return response

    def verify_otp(self, otp):
        data = {"otp": otp}
        response = requests.post(
            self.verify_otp_url, headers=self.headers, data=json.dumps(data)
        ).json()
        Constants.logger.info(response)
        return response

    @timeit(MetricName="Motilal:get_ltp")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
    )
    def get_ltp(self, exchange=None, tradingsymbol=None) -> float:
        tradingsymbol = self.get_symbol(tradingsymbol)
        token = self.symbol_data["{}:{}".format(exchange, tradingsymbol)]["token"]
        exchange = self.get_exchange(exchange)
        data = {
            "userid": self.user_id,
            "exchange": exchange,
            "scripcode": token,
        }

        Constants.logger.info("[GET_LTP_REQUEST] response {}".format(data))
        response = requests.post(
            self.ltp_utl, headers=self.headers, data=json.dumps(data)
        )
        Constants.logger.info("[GET_LTP_RESPONSE] response {}".format(response.json()))
        return response.json()["data"]["ltp"] / 100.0

    @timeit(MetricName="Motilal:modify_price")
    def modify_price(self, order_id, price, trigger_price=None, order_type=None):
        orders = self.orders()
        orders = orders[orders["order_id"] == order_id]

        if len(orders) != 1:
            Constants.logger.error(
                "[ORDER_NOT_FOUND] invalid modify request for {}".format(order_id)
            )
            return
        orders.loc[:, "last_modified_time"] = orders.last_modified_time.astype(str)
        order = orders.to_dict("records")[0]

        order["price"] = price
        if trigger_price is not None:
            order["trigger_price"] = trigger_price

        if order["order_type"] == "SL":
            order["order_type"] = "STOPLOSS"

        print(order)
        self.modify_order(order)

    @timeit(MetricName="Motilal:modify_order")
    def modify_order(self, order_to_modify: ModifyOrderRequest) -> str:
        order: dict = copy.deepcopy(order_to_modify)  # type:ignore
        data = {
            "uniqueorderid": order["order_id"],
            "newordertype": order["order_type"].upper(),
            "neworderduration": order["order_duration"].upper(),
            "newquantityinlot": int(order["pending_quantity"] / order["lot_size"]),
            # "newdisclosedquantity": 0,
            "newprice": order["price"],
        }

        if "trigger_price" in order:
            data["newtriggerprice"] = order["trigger_price"]
        if "quantity_traded_today" in order:
            data["qtytradedtoday"] = order["quantity_traded_today"]
        if "last_modified_time" in order:
            data["lastmodifiedtime"] = order["last_modified_time"]

        if "exchange" in order and order["exchange"] == "MCX":
            data["newquantityinlot"] = int(order["totalqtyremaining"])

        try:
            Constants.logger.info("[MODIFYING_ORDER] order [{}]".format(data))
            response = requests.post(
                self.modify_order_url, headers=self.headers, data=json.dumps(data)
            ).json()
            Constants.logger.info("[MODIFY_ORDER_RESPONSE] {}".format(response))
        except Exception as e:
            exception_message = (
                "[ORDER_MODIFICATION_FAILED] for {} failed with exception {}".format(
                    order["uniqueorderid"], e
                )
            )
            Constants.logger.error("{}".format(exception_message))
        return order["order_id"]

    @timeit(MetricName="Motilal:cancel_order")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=2,
        retry_on_exception=retry_exception,
    )
    def cancel_order(self, order_id: str, variety=None) -> None:
        data = {"uniqueorderid": order_id}

        try:
            Constants.logger.info("Cancelling order [{}]".format(order_id))
            response = requests.post(
                self.cancel_order_url, headers=self.headers, data=json.dumps(data)
            ).json()
            if "errorcode" in response and response["errorcode"] in ["MO1066"]:
                Constants.logger.info(
                    f"[CANCEL_ORDER_RESPONSE] [{order_id}] already cancelled"
                )
                return
            elif "errorcode" in response and response["errorcode"] in ["MO5002"]:
                raise RetryableException("Retry due to network error")
            elif "errorcode" in response and response["errorcode"] in ["MO1060"]:
                # Invalid order Id
                return
            Constants.logger.info("Cancel order response [{}]".format(response))
        except Exception as e:
            exception_message = (
                "[ORDER_CANCELLATION_FAILED] unique_order_id {} exception {}".format(
                    order_id, e
                )
            )
            Constants.logger.error(exception_message)

    def get_profile(self):
        response = requests.post(
            self.get_profile_url,
            headers=self.headers,
            data=json.dumps({"Clientcode": self.headers["vendorinfo"]}),
        ).json()
        if response["status"] == "ERROR":
            raise Exception(response["message"])

        return response["data"]

    @timeit(MetricName="Motilal:margins")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
    )
    def margins(self):
        response = requests.post(
            self.margin_summary_url,
            headers=self.headers,
            data=json.dumps({"Clientcode": self.headers["vendorinfo"]}),
        ).json()
        if response["status"] == "ERROR":
            raise Exception(response["message"])
        margin_summary = response["data"]

        margins = {"margin_used": 0, "margin_available": 0}
        for margin_particular in margin_summary:
            if margin_particular["srno"] in [103]:
                margins["margin_available"] += margin_particular["amount"]
            if margin_particular["srno"] in [301, 321, 340, 360]:
                margins["margin_used"] += margin_particular["amount"]

        return margins

    @timeit(MetricName="Motilal:place_order")
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
        order_type = self.get_order_type(order_type)
        product = self.get_product(product)
        tradingsymbol = self.get_symbol(tradingsymbol)

        actual_exchange = copy.deepcopy(exchange)
        if actual_exchange == "NSEFO":
            actual_exchange = "NFO"
        elif actual_exchange == "BSEFO":
            actual_exchange = "BFO"
        token = self.symbol_data["{}:{}".format(actual_exchange, tradingsymbol)]["token"]

        exchange = self.get_exchange(exchange)
        quantity = self.place_order_quantity(quantity, tradingsymbol, exchange)

        data = {
            "exchange": exchange,
            "symboltoken": token,
            "buyorsell": transaction_type,
            "ordertype": order_type,
            "producttype": product,
            "orderduration": "DAY",
            "price": price,
            "triggerprice": trigger_price,
            "quantityinlot": quantity,
            "disclosedquantity": 0,
            "amoorder": "N",
            "algoid": "",
            "tag": tag,
        }
        try:
            Constants.logger.info("[PLACING_ORDER] {}".format(json.dumps(data)))
            response = requests.post(
                self.place_order_url, headers=self.headers, data=json.dumps(data)
            ).json()
            if "errorcode" in response and response["errorcode"] in ["100018"]:
                return
            Constants.logger.info(
                "[PLACE_ORDER_RESPONSE] {} input {}".format(response, json.dumps(data))
            )
            if response["status"] == "ERROR":
                raise QuantplayOrderPlacementException(response["message"])
            return response["uniqueorderid"]
        except QuantplayOrderPlacementException as e:
            raise e
        except Exception as e:
            exception_message = "Order placement failed with error [{}]".format(str(e))
            print(exception_message)

    def on_message(self, ws, order):
        try:
            order = json.loads(order)

            order["placed_by"] = self.user_id
            order["tag"] = self.user_id
            order["order_id"] = order["orderid"]
            order["exchange_order_id"] = order["order_id"]
            order["transaction_type"] = order["transactiontype"]
            order["quantity"] = int(order["quantity"])
            order["order_type"] = order["ordertype"]

            if order["exchange"] == "NFO":
                order["tradingsymbol"] = self.symbol_map[  # type:ignore
                    order["tradingsymbol"]
                ]

            if order["order_type"] == "STOPLOSS_LIMIT":
                order["order_type"] = "SL"

            if "triggerprice" in order and order["triggerprice"] != 0:
                order["trigger_price"] = float(order["triggerprice"])
            else:
                order["trigger_price"] = None

            if order["status"] == "trigger pending":
                order["status"] = "TRIGGER PENDING"
            elif order["status"] == "cancelled":
                order["status"] = "CANCELLED"
            elif order["status"] == "open":
                order["status"] = "OPEN"
            elif order["status"] == "complete":
                order["status"] = "COMPLETE"

            # self.order_updates.put(order)
            print("Final order {}".format(order))
        except Exception as e:
            Constants.logger.error("[ORDER_UPDATE_PROCESSING_FAILED] {}".format(e))
        print(json.dumps(order))

    def on_error(self, ws, error):
        print(error)

    def on_close(self, ws):
        print("### closed ###")

    def on_open(self, ws):
        def run(*args):
            for i in range(300000):
                time.sleep(1)
                print(
                    {
                        "actiontype": "TradeSubscribe",
                        "clientid": self.headers["vendorinfo"],
                    }
                )
                ws.send(
                    json.dumps(
                        {
                            "actiontype": "TradeSubscribe",
                            "clientid": self.headers["vendorinfo"],
                        }
                    )
                )
            time.sleep(1)
            ws.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())

    @timeit(MetricName="Motilal:account_summary")
    def account_summary(self):
        response = self.margins()
        response["pnl"] = float(self.positions()["pnl"].sum())  # type: ignore

        return response

    @timeit(MetricName="Motilal:profile")
    def profile(self) -> UserBrokerProfileResponse:
        api_response = requests.post(
            self.get_profile_url,
            headers=self.headers,
            data=json.dumps({"Clientcode": self.headers["vendorinfo"]}),
        ).json()
        if api_response["status"] == "ERROR":
            raise Exception(api_response["message"])

        api_response = api_response["data"]
        response: UserBrokerProfileResponse = {
            "user_id": api_response["clientcode"],
            "full_name": api_response["name"],
            "segments": api_response["exchanges"],
        }

        return response

    @timeit(MetricName="Motilal:holdings")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
    )
    def holdings(self):
        response = (requests.post(self.holdings_url, headers=self.headers)).json()
        if response["status"] == "ERROR":
            Constants.logger.info(
                "Error while fetching order book [{}]".format(response["message"])
            )
            raise Exception(response["message"])

        holdings = response["data"]

        if holdings is None or len(holdings) == 0:
            return pl.DataFrame(schema=self.holidings_schema)

        holdings_df = pl.DataFrame(holdings)
        holdings_df = holdings_df.rename(
            {
                "scripname": "tradingsymbol",
                "scripisinno": "isin",
                "nsesymboltoken": "token",
                "buyavgprice": "average_price",
                "dpquantity": "quantity",
                "collateralquantity": "pledged_quantity",
            }
        )
        holdings_df = holdings_df.with_columns(pl.lit("NSE").alias("exchange"))
        holdings_df = holdings_df.with_columns(
            pl.struct(["exchange", "tradingsymbol"])
            .map_elements(
                lambda x: int(self.get_ltp(x["exchange"], x["tradingsymbol"])),
                return_dtype=pl.Float64,
            )
            .alias("price")
        )

        holdings_df = holdings_df.with_columns(
            pl.col("tradingsymbol").str.replace(" EQ", "").alias("tradingsymbol")
        )
        holdings_df = holdings_df.with_columns(
            (pl.col("quantity") * pl.col("price")).alias("value"),
            pl.lit(0).alias("pledged_quantity"),
            (pl.col("quantity") * pl.col("average_price")).alias("buy_value"),
            (pl.col("quantity") * pl.col("price")).alias("current_value"),
            ((pl.col("price") / pl.col("average_price") - 1) * 100).alias("pct_change"),
        )

        return holdings_df[list(self.holidings_schema.keys())].cast(self.holidings_schema)

    @timeit(MetricName="Motilal:positions")
    @retry(
        wait_exponential_multiplier=3000,
        wait_exponential_max=10000,
        stop_max_attempt_number=3,
    )
    def positions(self, drop_cnc: bool = True) -> pl.DataFrame:
        response = (requests.post(self.positions_url, headers=self.headers)).json()
        if response["status"] == "ERROR":
            Constants.logger.info(
                "Error while fetching positions [{}]".format(response["message"])
            )
            raise Exception(response["message"])

        positions = response["data"]

        if positions is None or len(positions) == 0:
            return pl.DataFrame(schema=self.positions_schema)

        positions_df = pl.DataFrame(positions)
        positions_df = positions_df.rename(
            {
                "symbol": "tradingsymbol",
                "LTP": "ltp",
                "productname": "product",
                "sellquantity": "sell_quantity",
                "buyquantity": "buy_quantity",
                "sellamount": "sell_value",
                "buyamount": "buy_value",
                "optiontype": "option_type",
                "symboltoken": "token",
            }
        )

        positions_df = positions_df.with_columns(
            (pl.col("sell_value") - pl.col("buy_value")).alias("pnl")
        )
        positions_df = positions_df.with_columns(
            (
                pl.col("pnl")
                + (pl.col("buy_quantity") - pl.col("sell_quantity")) * pl.col("ltp")
            ).alias("pnl")
        )
        positions_df = positions_df.with_columns(
            (pl.col("buy_quantity") - pl.col("sell_quantity")).alias("quantity")
        )

        positions_df = positions_df.with_columns(
            pl.when(pl.col("exchange") == "NSEFO")
            .then(pl.lit("NFO"))
            .when(pl.col("exchange") == "BSEFO")
            .then(pl.lit("BFO"))
            .otherwise(pl.col("exchange"))
            .alias("exchange")
        )

        positions_df = positions_df.with_columns(
            pl.col("product").str.replace("NORMAL", "NRML").alias("product")
        )
        positions_df = positions_df.with_columns(
            ((pl.col("buy_value") - pl.col("sell_value")) / pl.col("quantity")).alias(
                "average_price"
            )
        )
        positions_df = positions_df.with_columns(
            pl.when(pl.col("quantity") == 0)
            .then(0)
            .otherwise(pl.col("average_price"))
            .alias("average_price")
        )

        return positions_df[list(self.positions_schema.keys())].cast(
            self.positions_schema
        )

    @timeit(MetricName="Motilal:orders")
    def orders(self, tag: str | None = None, add_ltp: bool = True) -> pl.DataFrame:
        response = (requests.post(self.order_book_url, headers=self.headers)).json()
        if response["status"] == "ERROR":
            Constants.logger.info(
                "Error while fetching order book [{}]".format(response["message"])
            )
            raise Exception(response["message"])
        orders = response["data"]

        if orders is None or len(orders) == 0:
            return pl.DataFrame(schema=self.orders_schema)

        orders_df = pl.DataFrame(orders)
        orders_df = orders_df.rename(
            {
                "symbol": "tradingsymbol",
                "producttype": "product",
                "clientid": "user_id",
                "symboltoken": "token",
                "buyorsell": "transaction_type",
                "averageprice": "average_price",
                "uniqueorderid": "order_id",
                "orderstatus": "status",
                "recordinserttime": "order_timestamp",
                "orderqty": "quantity",
                "triggerprice": "trigger_price",
                "totalqtytraded": "filled_quantity",
                "totalqtyremaining": "pending_quantity",
                "orderduration": "order_duration",
                "lastmodifiedtime": "last_modified_time",
                "qtytradedtoday": "quantity_traded_today",
                "lotsize": "lot_size",
                "ordertype": "order_type",
            }
        )
        if add_ltp:
            positions = self.positions()
            positions = positions.sort("product").group_by("tradingsymbol").head(1)

            if "ltp" in orders_df.columns:
                orders_df = orders_df.drop(["ltp"])
            orders_df = orders_df.join(
                positions.select(["tradingsymbol", "ltp"]), on="tradingsymbol", how="left"
            )

        orders_df = orders_df.with_columns(
            pl.when(pl.col("product") == "VALUEPLUS")
            .then(pl.lit("MIS"))
            .when(pl.col("product") == "DELIVERY")
            .then(pl.lit("CNC"))
            .when(pl.col("product") == "NORMAL")
            .then(pl.lit("NRML"))
            .otherwise(pl.col("product"))
            .alias("product")
        )

        orders_df = orders_df.filter(pl.col("last_modified_time") != "0")

        orders_df = orders_df.with_columns(
            pl.col("last_modified_time")
            .str.to_datetime("%d-%b-%Y %H:%M:%S")
            .alias("update_timestamp")
        )

        orders_df = orders_df.with_columns(
            (
                pl.col("ltp") * pl.col("filled_quantity")
                - pl.col("average_price") * pl.col("filled_quantity")
            ).alias("pnl")
        )

        orders_df = orders_df.with_columns(
            pl.when(pl.col("transaction_type") == "SELL")
            .then(-pl.col("pnl"))
            .otherwise(pl.col("pnl"))
            .alias("pnl")
        )

        orders_df = orders_df.with_columns(
            pl.when((pl.col("status") == "Confirm") & (pl.col("trigger_price") > 0))
            .then(pl.lit("TRIGGER PENDING"))
            .otherwise(pl.col("status"))
            .alias("status")
        )

        orders_df = orders_df.with_columns(
            pl.when((pl.col("status") == "Confirm") & (pl.col("trigger_price") == 0))
            .then(pl.lit("OPEN"))
            .otherwise(pl.col("status"))
            .alias("status")
        )

        if tag:
            orders_df = orders_df.filter(pl.col("tag") == tag)

        orders_df = orders_df.with_columns(
            pl.when(pl.col("status") == "Traded")
            .then(pl.lit("COMPLETE"))
            .when(pl.col("status") == "Error")
            .then(pl.lit("REJECTED"))
            .when(pl.col("status") == "Cancel")
            .then(pl.lit("CANCELLED"))
            .when(pl.col("status") == "Rejected")
            .then(pl.lit("REJECTED"))
            .otherwise(pl.col("status"))
            .alias("status")
        )

        orders_df = orders_df.with_columns(
            pl.when(pl.col("order_type") == "Stop Loss")
            .then(pl.lit("SL"))
            .otherwise(pl.col("order_type").str.to_uppercase())
            .alias("order_type")
        )

        orders_df = orders_df.with_columns(
            pl.when(pl.col("exchange") == "NSEFO")
            .then(pl.lit("NFO"))
            .when(pl.col("exchange") == "NSECD")
            .then(pl.lit("CDS"))
            .when(pl.col("exchange") == "BSEFO")
            .then(pl.lit("BFO"))
            .otherwise(pl.col("exchange"))
            .alias("exchange")
        )
        orders_df = orders_df.with_columns(
            pl.col("order_timestamp")
            .str.to_datetime("%d-%b-%Y %H:%M:%S")
            .alias("order_timestamp")
        )

        orders_schema = copy.deepcopy(self.orders_schema)
        orders_schema["last_modified_time"] = pl.String
        orders_schema["order_duration"] = pl.String
        orders_schema["quantity_traded_today"] = pl.Int64
        orders_schema["lot_size"] = pl.Int64
        orders_df = orders_df.with_columns(pl.lit("regular").alias("variety"))
        orders_df = orders_df.with_columns(pl.lit("").alias("status_message"))
        orders_df = orders_df.with_columns(pl.lit("").alias("status_message_raw"))

        return orders_df[list(orders_schema.keys())].cast(orders_schema)
