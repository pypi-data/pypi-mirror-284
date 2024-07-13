import logging
import decimal
from functools import wraps
import time
from typing import Any
import numpy as np
import json
from datetime import datetime


formatter = logging.Formatter(
    "%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s"
)


class LoggerUtils:
    @staticmethod
    def get_log_file_path(file_name: str) -> str:
        today_date = datetime.now()

        return "/tmp/" + file_name + "-" + today_date.strftime("%Y-%m-%d:01") + ".log"

    @staticmethod
    def setup_logger(
        logger_name: str, log_file: str, level=logging.DEBUG
    ) -> logging.Logger:
        log_file = LoggerUtils.get_log_file_path(log_file)
        """Function setup as many loggers as you want"""

        handler = logging.FileHandler(log_file)
        handler.setFormatter(formatter)

        logger = logging.getLogger(logger_name)
        logger.setLevel(level)
        logger.addHandler(handler)
        logger.propagate = False
        logger.disabled = False

        return logger


class Constants:
    logger = LoggerUtils.setup_logger("main_logger", "trading")
    latency_logger = LoggerUtils.setup_logger("latency", "latency")
    order_execution_logger = LoggerUtils.setup_logger(
        "order_execution", "order_execution"
    )
    historical_data_logger = LoggerUtils.setup_logger(
        "hist_data_looger", "historical_data"
    )
    tick_logger = LoggerUtils.setup_logger("tick_logger", "tick")

    @staticmethod
    def myconverter(o: Any):
        if isinstance(o, datetime):
            return o.__str__()
        if isinstance(o, decimal.Decimal):
            return float(o)
        if isinstance(o, np.int64):  # type:ignore
            return int(o)

    @staticmethod
    def round_to_tick(number: int | float) -> float:
        return round(number * 20) / 20


class OrderType:
    market = "MARKET"
    slm = "SL-M"
    sl = "SL"
    limit = "LIMIT"


class OrderStatus:
    complete = "COMPLETE"
    cancelled = "CANCELLED"
    open = "OPEN"
    rejected = "REJECTED"
    trigger_pending = "TRIGGER PENDING"
    modify_validation_pending = "MODIFY VALIDATION PENDING"
    validation_pending = "VALIDATION PENDING"


def timeit(*args_main, **kwargs_main):
    def inner_function(function):
        @wraps(function)
        def wrapper(*args, **kwargs):
            ts = time.time()
            result = function(*args, **kwargs)
            te = time.time()
            if "MetricName" in kwargs_main:
                data = {
                    "MetricName": kwargs_main["MetricName"],
                    "Unit": "Seconds",
                    "Value": (te - ts),
                }
                Constants.latency_logger.info(f"{json.dumps(data)}")
            else:
                Constants.logger.error(f"No metric found in {function.__name__}")
            return result

        return wrapper

    return inner_function
