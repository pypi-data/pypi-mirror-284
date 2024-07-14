from typing import Optional
import hashlib
import hmac
import inspect
import numpy as np
from time import sleep, time
from datetime import datetime, timezone
from requests import get, post
from quantfreedom.core.enums import (
    ExchangeSettings,
    FootprintCandlesTuple,
    LeverageModeType,
    PositionModeType,
    TriggerDirectionType,
)

from quantfreedom.exchanges.exchange import UNIVERSAL_TIMEFRAMES, Exchange

BYBIT_TIMEFRAMES = ["1", "5", "15", "30", "60", "120", "240", "360", "720", "D", "W"]


class Bybit(Exchange):
    def __init__(
        # Exchange Vars
        self,
        use_testnet: bool,
        api_key: str = None,
        secret_key: str = None,
    ):
        """
        main docs page https://bybit-exchange.github.io/docs/v5/intro
        [upgrade to unified account](https://www.bybit.com/en/help-center/article/UTA-guide#cb)
        """
        if api_key:
            self.api_key = api_key
            self.secret_key = secret_key

        if use_testnet:
            self.url_start = "https://api-testnet.bybit.com"
        else:
            self.url_start = "https://api.bybit.com"
            self.ws_url_start = "wss://stream.bybit.com/v5/public"

    """
    ################################################################
    ################################################################
    ###################                          ###################
    ###################                          ###################
    ################### Sending Info Functionsns ###################
    ###################                          ###################
    ###################                          ###################
    ################################################################
    ################################################################
    """

    def __HTTP_post_request(self, end_point: str, params: dict):
        str_timestamp = str(int(time() * 1000))
        params_as_dict_string = self.get_params_as_dict_string(params=params)
        signature = self.__gen_signature(str_timestamp=str_timestamp, params_as_string=params_as_dict_string)
        headers = {
            "X-BAPI-API-KEY": self.api_key,
            "X-BAPI-SIGN": signature,
            "X-BAPI-SIGN-TYPE": "2",
            "X-BAPI-TIMESTAMP": str_timestamp,
            "X-BAPI-RECV-WINDOW": "5000",
            "Content-Type": "application/json",
            "referer": "Rx000377",
        }

        try:
            response = post(
                url=self.url_start + end_point,
                headers=headers,
                data=params_as_dict_string,
            )
            response_json = response.json()
            return response_json
        except Exception as e:
            raise Exception(f"Bybit __HTTP_post_request - > {e}")

    def __HTTP_get_request(self, end_point: str, params: dict):
        str_timestamp = str(int(time() * 1000))
        params_as_path = self.get_params_as_path(params=params)
        signature = self.__gen_signature(str_timestamp=str_timestamp, params_as_string=params_as_path)
        headers = {
            "X-BAPI-API-KEY": self.api_key,
            "X-BAPI-SIGN": signature,
            "X-BAPI-SIGN-TYPE": "2",
            "X-BAPI-TIMESTAMP": str_timestamp,
            "X-BAPI-RECV-WINDOW": "5000",
            "Content-Type": "application/json",
        }

        try:
            response = get(
                url=self.url_start + end_point + "?" + params_as_path,
                headers=headers,
            )
            response_json = response.json()
            return response_json
        except Exception as e:
            raise Exception(f"Bybit __HTTP_get_request - > {e}")

    def __gen_signature(self, str_timestamp: str, params_as_string: str):
        param_str = str_timestamp + self.api_key + "5000" + params_as_string
        hash = hmac.new(bytes(self.secret_key, "utf-8"), param_str.encode("utf-8"), hashlib.sha256)
        return hash.hexdigest()

    """
    ###################################################################
    ###################################################################
    ###################                             ###################
    ###################                             ###################
    ################### Functions no default params ###################
    ###################                             ###################
    ###################                             ###################
    ###################################################################
    ###################################################################
    """

    def get_exchange_timeframe(
        self,
        timeframe: str,
    ):
        try:
            return BYBIT_TIMEFRAMES[UNIVERSAL_TIMEFRAMES.index(timeframe)]
        except Exception as e:
            raise Exception(f"Use one of these timeframes - {UNIVERSAL_TIMEFRAMES} -> {e}")

    def get_candles(
        self,
        symbol: str,
        timeframe: str,
        since_datetime: datetime = None,
        until_datetime: datetime = None,
        candles_to_dl: int = 1000,
        category: str = "linear",
    ) -> FootprintCandlesTuple:
        """
        Summary
        -------
        [Bybit candle docs](https://bybit-exchange.github.io/docs/v5/market/kline)

        Explainer Video
        ---------------
        Coming Soon but if you want/need it now please let me know in discord or telegram and i will make it for you

        Parameters
        ----------
        symbol : str
            [Use Bybit API for symbol list](https://bybit-exchange.github.io/docs/v5/intro)
        timeframe : str
            "1m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "12h", "d", "w"
        since_datetime : datetime
            The start date, in datetime format, of candles you want to download. EX: datetime(year, month, day, hour, minute)
        until_datetime : datetime
            The until date, in datetime format, of candles you want to download minus one candle so if you are on the 5 min if you say your until date is 1200 your last candle will be 1155. EX: datetime(year, month, day, hour, minute)
        candles_to_dl : int
            The amount of candles you want to download
        category : str
            [Bybit categories link](https://bybit-exchange.github.io/docs/v5/enum#category)

        Returns
        -------
        np.array
            a 2 dim array with the following columns "timestamp", "open", "high", "low", "close", "volume"
        """
        ex_timeframe = self.get_exchange_timeframe(timeframe=timeframe)
        self.timeframe_in_ms = self.get_timeframe_in_ms(timeframe=timeframe)
        candles_to_dl_ms = candles_to_dl * self.timeframe_in_ms

        since_timestamp, until_timestamp = self.get_since_until_timestamp(
            candles_to_dl_ms=candles_to_dl_ms,
            since_datetime=since_datetime,
            timeframe_in_ms=self.timeframe_in_ms,
            until_datetime=until_datetime,
        )

        candles_list = []
        end_point = "/v5/market/kline"
        params = {
            "category": category,
            "symbol": symbol,
            "interval": ex_timeframe,
            "start": since_timestamp,
            "end": until_timestamp,
            "limit": 1000,
        }

        waiter_timestamp = until_timestamp + 5000 - (self.timeframe_in_ms * 2)
        # add 5 seconds back so it is a flat time, then subtract the timeframe * two

        while params["end"] - self.timeframe_in_ms > since_timestamp:
            try:
                response: dict = get(url=self.url_start + end_point, params=params).json()
                new_candles = response["result"]["list"]

                first_candle_timestamp = int(new_candles[0][0])
                last_candle_timestamp = int(new_candles[-1][0])

                if first_candle_timestamp == waiter_timestamp:
                    # checking to see if the first candle we download is one candle behind what we should be downloading
                    # if it is then we are trying to dl candles too soon and need to wait to try again
                    print("sleeping .2 seconds")
                    sleep(0.2)
                else:
                    candles_list.extend(new_candles)
                    # add 2 sec so we don't download the same candle two times
                    params["end"] = last_candle_timestamp - 2000

            except Exception as e:
                raise Exception(f"Bybit get_candles {response.get('message')} - > {e}")

        candles = np.flip(np.array(candles_list, dtype=np.float_)[:, :-1], axis=0)
        open_timestamps = candles[:, 0].astype(np.int64)

        Footprint_Candles_Tuple = FootprintCandlesTuple(
            candle_open_datetimes=open_timestamps.astype("datetime64[ms]"),
            candle_open_timestamps=open_timestamps,
            candle_durations_seconds=np.full(candles.shape[0], int(self.timeframe_in_ms / 1000)),
            candle_open_prices=candles[:, 1],
            candle_high_prices=candles[:, 2],
            candle_low_prices=candles[:, 3],
            candle_close_prices=candles[:, 4],
            candle_asset_volumes=candles[:, 5],
            candle_usdt_volumes=np.around(a=candles[:, 5] * candles[:, 4], decimals=3),
        )
        self.last_fetched_ms_time = int(candles[-1, 0])

        return Footprint_Candles_Tuple

    def create_order(
        self,
        symbol: str,
        buy_sell: str,
        position_mode: int,
        order_type: str,
        asset_size: float,
        category: str = "linear",
        time_in_force: str = "GTC",
        price: Optional[float] = None,
        triggerDirection: Optional[int] = None,
        triggerPrice: Optional[float] = None,
        triggerBy: str = None,
        tpTriggerBy: str = None,
        slTriggerBy: str = None,
        custom_order_id: str = None,
        takeProfit: Optional[float] = None,
        stopLoss: Optional[float] = None,
        reduce_only: bool = None,
        closeOnTrigger: bool = None,
        isLeverage: Optional[int] = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/order/create-order
        """
        end_point = "/v5/order/create"
        params = {}
        params["symbol"] = symbol.upper()
        params["side"] = buy_sell.capitalize()
        params["category"] = category
        params["isLeverage"] = isLeverage
        params["positionIdx"] = position_mode
        params["orderType"] = order_type.capitalize()
        params["qty"] = str(asset_size)
        params["price"] = str(price) if price else price
        params["triggerDirection"] = triggerDirection
        params["triggerPrice"] = str(triggerPrice) if triggerPrice else triggerPrice
        params["triggerBy"] = triggerBy
        params["tpTriggerBy"] = tpTriggerBy
        params["slTriggerBy"] = slTriggerBy
        params["timeInForce"] = time_in_force
        params["orderLinkId"] = custom_order_id
        params["takeProfit"] = str(takeProfit) if takeProfit else takeProfit
        params["stopLoss"] = str(stopLoss) if stopLoss else stopLoss
        params["reduceOnly"] = reduce_only
        params["closeOnTrigger"] = closeOnTrigger

        response = self.__HTTP_post_request(end_point=end_point, params=params)
        try:
            order_id = response["result"]["orderId"]
            return order_id
        except Exception as e:
            raise Exception(f"Bybit create_order {response['retMsg']} -> {e}")

    def create_long_hedge_mode_entry_market_order_with_stoploss(
        self,
        asset_size: float,
        symbol: str,
        sl_price: float,
    ):
        return self.create_order(
            symbol=symbol,
            position_mode=PositionModeType.BuySide,
            buy_sell="Buy",
            order_type="Market",
            asset_size=asset_size,
            time_in_force="GTC",
            stopLoss=sl_price,
        )

    def create_long_hedge_mode_entry_market_order(
        self,
        asset_size: float,
        symbol: str,
    ):
        return self.create_order(
            symbol=symbol,
            position_mode=PositionModeType.BuySide,
            buy_sell="Buy",
            order_type="Market",
            asset_size=asset_size,
            time_in_force="GTC",
        )

    def create_long_hedge_mode_tp_limit_order(
        self,
        asset_size: float,
        symbol: str,
        tp_price: float,
    ):
        return self.create_order(
            symbol=symbol,
            position_mode=PositionModeType.BuySide,
            buy_sell="Sell",
            order_type="Limit",
            asset_size=asset_size,
            price=tp_price,
            reduce_only=True,
            time_in_force="PostOnly",
        )

    def create_long_hedge_mode_sl_order(
        self,
        asset_size: float,
        symbol: str,
        sl_price: float,
    ):
        return self.create_order(
            symbol=symbol,
            position_mode=PositionModeType.BuySide,
            buy_sell="Sell",
            order_type="Market",
            asset_size=asset_size,
            triggerPrice=sl_price,
            reduce_only=True,
            triggerDirection=TriggerDirectionType.Fall,
            time_in_force="GTC",
        )

    def get_position_info(
        self,
        symbol: str = None,
        baseCoin: str = None,
        category: str = "linear",
        limit: int = 50,
        settleCoin: str = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/position
        """
        end_point = "/v5/position/list"
        params = {}
        params["symbol"] = symbol
        params["limit"] = limit
        params["settleCoin"] = settleCoin
        params["baseCoin"] = baseCoin
        params["category"] = category
        response: dict = self.__HTTP_get_request(end_point=end_point, params=params)
        try:

            data_list = response["result"]["list"]

            return data_list
        except Exception as e:
            raise Exception(f"Bybit get_account_position_info = Data or List is empty {response['retMsg']} -> {e}")

    def get_long_hedge_mode_position_info(
        self,
        symbol: str,
    ):
        pos_info = self.get_position_info(symbol=symbol)[0]
        return pos_info

    def get_wallet_info(
        self,
        accountType: str = "UNIFIED",
        trading_with: str = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/account/wallet-balance
        """
        end_point = "/v5/account/wallet-balance"

        params = {}
        params["accountType"] = accountType
        params["coin"] = trading_with

        response: dict = self.__HTTP_get_request(end_point=end_point, params=params)
        try:
            data_list = response["result"]["list"]
            data_list[0]
            return data_list
        except Exception as e:
            raise Exception(f"Bybit get_wallet_info = Data or List is empty {response['retMsg']} -> {e}")

    def get_no_fees_balance_of_asset_market_in_only(
        self,
        trading_with: str,
        symbol: str,
        accountType: str = "UNIFIED",
    ):
        coins = self.get_wallet_info(accountType=accountType, trading_with=trading_with)[0]["coin"]
        for coin in coins:
            if coin["coin"] == trading_with:
                wallet_balance = float(coin["walletBalance"])
                break

        market_fee_pct = self.get_fee_pcts(symbol=symbol)[0]
        pos_info = self.get_position_info(symbol=symbol)

        long_pos_value = pos_info[0]["positionValue"]
        long_fees = float(long_pos_value) * market_fee_pct if long_pos_value else 0

        short_pos_value = pos_info[1]["positionValue"]
        short_fees = float(short_pos_value) * market_fee_pct if short_pos_value else 0

        total_fees = long_fees + short_fees

        no_fee_wallet_balance = wallet_balance + total_fees

        return no_fee_wallet_balance

    def upgrade_to_unified_trading_account(self):
        end_point = "/v5/account/upgrade-to-uta"
        params = {}

        response: dict = self.__HTTP_post_request(end_point=end_point, params=params)
        try:
            return response["retMsg"]

        except Exception as e:
            raise Exception(f"Data or List is empty {response['retMsg']} -> {e}")

    def get_closed_pnl(
        self,
        symbol: str,
        limit: int = 50,
        since_datetime: datetime = None,
        until_datetime: datetime = None,
        category: str = "linear",
    ):
        """
        [Bybit API link to Get Closed Profit and Loss](https://bybit-exchange.github.io/docs/v5/position/close-pnl)
        """

        if since_datetime is not None:
            since_datetime = int(since_datetime.replace(tzinfo=timezone.utc).timestamp() * 1000)
        if until_datetime is not None:
            until_datetime = int(until_datetime.replace(tzinfo=timezone.utc).timestamp() * 1000)

        end_point = "/v5/position/closed-pnl"
        params = {}
        params["category"] = category
        params["symbol"] = symbol
        params["limit"] = limit
        params["startTime"] = since_datetime
        params["endTime"] = until_datetime

        response: dict = self.__HTTP_get_request(end_point=end_point, params=params)
        try:
            response["result"]["list"][0]
            data_list = response["result"]["list"]
            return data_list
        except Exception as e:
            raise Exception(f"Data or List is empty {response['retMsg']} -> {e}")

    def get_latest_pnl_result(
        self,
        symbol: str,
        category: str = "linear",
    ):
        return float(self.get_closed_pnl(category=category, symbol=symbol)[0]["closedPnl"])

    def get_order_history(
        self,
        baseCoin: str = None,
        category: str = "linear",
        custom_order_id: str = None,
        limit: int = 50,
        orderFilter: str = None,
        orderStatus: str = None,
        order_id: str = None,
        settleCoin: str = None,
        since_datetime: datetime = None,
        symbol: str = None,
        until_datetime: datetime = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/order/order-list
        """
        if since_datetime is not None:
            since_datetime = int(since_datetime.replace(tzinfo=timezone.utc).timestamp() * 1000)
        if until_datetime is not None:
            until_datetime = int(until_datetime.replace(tzinfo=timezone.utc).timestamp() * 1000)

        end_point = "/v5/order/history"
        params = {}
        params["baseCoin"] = baseCoin
        params["category"] = category
        params["endTime"] = until_datetime
        params["limit"] = limit
        params["orderFilter"] = orderFilter
        params["orderId"] = order_id
        params["orderLinkId"] = custom_order_id
        params["orderStatus"] = orderStatus
        params["settleCoin"] = settleCoin
        params["startTime"] = since_datetime
        params["symbol"] = symbol
        response: dict = self.__HTTP_get_request(end_point=end_point, params=params)
        try:
            data_list = response["result"]["list"]
            data_list[0]  # try this to see if anything is in here
            return data_list
        except Exception as e:
            raise Exception(f"Bybit get_order_history = Data or List is empty {response['retMsg']} -> {e}")

    def get_open_orders(
        self,
        symbol: str,
        baseCoin: str = None,
        category: str = "linear",
        custom_order_id: str = None,
        limit: int = 50,
        orderFilter: str = None,
        orderStatus: str = None,
        order_id: str = None,
        settleCoin: str = None,
        since_datetime: datetime = None,
        until_datetime: datetime = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/order/open-order
        """
        if since_datetime is not None:
            since_datetime = int(since_datetime.replace(tzinfo=timezone.utc).timestamp() * 1000)
        if until_datetime is not None:
            until_datetime = int(until_datetime.replace(tzinfo=timezone.utc).timestamp() * 1000)

        end_point = "/v5/order/realtime"
        params = {}
        params["baseCoin"] = baseCoin
        params["category"] = category
        params["endTime"] = until_datetime
        params["limit"] = limit
        params["orderFilter"] = orderFilter
        params["orderId"] = order_id
        params["orderLinkId"] = custom_order_id
        params["orderStatus"] = orderStatus
        params["settleCoin"] = settleCoin
        params["startTime"] = since_datetime
        params["symbol"] = symbol
        response: dict = self.__HTTP_get_request(end_point=end_point, params=params)
        try:
            data_list = response["result"]["list"]
            return data_list
        except Exception as e:
            raise Exception(f"Bybit get_open_orders = {response['retMsg']} -> {e}")

    def check_if_order_open(
        self,
        order_id: str,
        symbol: str = None,
    ):
        data_list = self.get_open_orders(order_id=order_id, symbol=symbol)
        try:
            if data_list[0]["orderId"] == order_id:
                return True
            else:
                raise Exception
        except Exception as e:
            raise Exception(f"Bybit check_if_order_canceled -> {e}")

    def get_filled_order_by_order_id(
        self,
        order_id: str,
        symbol: str = None,
    ):
        filled_order = self.get_open_orders(order_id=order_id, symbol=symbol)[0]
        return filled_order

    def get_open_order_by_order_id(
        self,
        order_id: str,
        symbol: str = None,
    ):
        open_order = self.get_open_orders(order_id=order_id, symbol=symbol)[0]
        return open_order

    def check_if_order_filled(
        self,
        order_id: str,
        symbol: str = None,
    ):
        data_dict = self.get_filled_order_by_order_id(order_id=order_id, symbol=symbol)
        try:
            if data_dict["orderId"] == order_id:
                return True
            else:
                raise Exception
        except Exception as e:
            raise Exception(f"bybit check_if_order_filled -> {e}")

    def cancel_all_open_orders(
        self,
        symbol: str = None,
        category: str = "linear",
        baseCoin: str = None,
        settleCoin: str = None,
        orderFilter: str = None,
        stopOrderType: str = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/order/cancel-all
        """
        end_point = "/v5/order/cancel-all"
        params = {}
        params["symbol"] = symbol
        params["stopOrderType"] = stopOrderType
        params["orderFilter"] = orderFilter
        params["settleCoin"] = settleCoin
        params["baseCoin"] = baseCoin
        params["category"] = category
        try:
            response: dict = self.__HTTP_post_request(end_point=end_point, params=params)
            if response["retMsg"] == "OK":
                return True
            else:
                raise Exception
        except Exception as e:
            raise Exception(f"Bybit cancel_all_open_orders_per_symbol message = {response['retMsg']} -> {e}")

    def cancel_all_open_orders_per_symbol(
        self,
        symbol: str,
    ):
        return self.cancel_all_open_orders(symbol=symbol)

    def set_leverage(
        self,
        symbol: str,
        leverage: float,
        category: str = "linear",
    ):
        """
        https://bybit-exchange.github.io/docs/v5/position/leverage
        """
        end_point = "/v5/position/set-leverage"
        leverage_str = str(leverage)

        params = {}
        params["symbol"] = symbol
        params["category"] = category
        params["buyLeverage"] = leverage_str
        params["sellLeverage"] = leverage_str

        response: dict = self.__HTTP_post_request(end_point=end_point, params=params)
        try:
            if response["retMsg"] in ["OK", "Set leverage not modified", "leverage not modified"]:
                return True
            else:
                raise Exception
        except Exception as e:
            raise Exception(f"Bybit set_leverage = Data or List is empty {response['retMsg']} -> {e}")

    def set_leverage_mode(
        self,
        setMarginMode: str = "ISOLATED_MARGIN",
    ):
        """
        https://bybit-exchange.github.io/docs/v5/account/set-margin-mode
        ISOLATED_MARGIN, REGULAR_MARGIN(i.e. Cross margin), PORTFOLIO_MARGIN
        """
        end_point = "/v5/account/set-margin-mode"
        params = {}
        params["setMarginMode"] = setMarginMode
        response: dict = self.__HTTP_post_request(end_point=end_point, params=params)
        try:
            if response["retMsg"] == "Request accepted":
                return True
            else:
                raise Exception
        except Exception as e:
            raise Exception(f"Bybit set_leverage_mode = Data or List is empty {response['retMsg']} -> {e}")

    def adjust_order(
        self,
        symbol: str,
        asset_size: Optional[float] = None,
        category: str = "linear",
        custom_order_id: str = None,
        orderIv: str = None,
        order_id: str = None,
        price: Optional[float] = None,
        slLimitPrice: Optional[float] = None,
        slTriggerBy: Optional[float] = None,
        stopLoss: Optional[float] = None,
        takeProfit: Optional[float] = None,
        tpLimitPrice: Optional[float] = None,
        tpslMode: str = None,
        tpTriggerBy: Optional[float] = None,
        triggerBy: Optional[float] = None,
        triggerPrice: Optional[float] = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/order/amend-order
        """
        end_point = "/v5/order/amend"
        params = {}
        params["category"] = category
        params["orderId"] = order_id
        params["orderIv"] = orderIv
        params["orderLinkId"] = custom_order_id
        params["price"] = str(price) if price else price
        params["qty"] = str(asset_size)
        params["slLimitPrice"] = str(slLimitPrice) if slLimitPrice else slLimitPrice
        params["slTriggerBy"] = str(slTriggerBy) if slTriggerBy else slTriggerBy
        params["stopLoss"] = str(stopLoss) if stopLoss else stopLoss
        params["symbol"] = symbol.upper()
        params["takeProfit"] = str(takeProfit) if takeProfit else takeProfit
        params["tpLimitPrice"] = str(tpLimitPrice) if tpLimitPrice else tpLimitPrice
        params["tpLimitPrice"] = str(tpLimitPrice) if tpLimitPrice else tpLimitPrice
        params["tpslMode"] = tpslMode
        params["tpTriggerBy"] = str(tpTriggerBy) if tpTriggerBy else tpTriggerBy
        params["triggerBy"] = str(triggerBy) if triggerBy else triggerBy
        params["triggerPrice"] = str(triggerPrice) if triggerPrice else triggerPrice

        response: dict = self.__HTTP_post_request(end_point=end_point, params=params)
        try:
            response_order_id = response["result"]["orderId"]
            if response_order_id == order_id or response["retMsg"] == "OK":
                return True
            else:
                raise Exception
        except Exception as e:
            raise Exception(f"bybit adjust_order message = {response['retMsg']} -> {e}")

    def move_stop_order(
        self,
        asset_size: float,
        new_price: float,
        order_id: str,
        symbol: str,
    ):
        return self.adjust_order(
            asset_size=asset_size,
            symbol=symbol,
            order_id=order_id,
            triggerPrice=new_price,
        )

    def get_risk_limit_info(
        self,
        symbol: str,
        category: str = "linear",
    ):
        """
        [Bybit API link to Get Risk Limit](https://bybit-exchange.github.io/docs/v5/market/risk-limit)
        """
        end_point = "/v5/market/risk-limit"
        params = {}
        params["symbol"] = symbol
        params["category"] = category

        response: dict = self.__HTTP_get_request(end_point=end_point, params=params)
        try:
            data_list = response["result"]["list"][0]

            return data_list
        except Exception as e:
            raise Exception(f"Bybit get_risk_limit_info = Data or List is empty {response['retMsg']} -> {e}")

    def __get_mmr_pct(
        self,
        symbol: str,
        category: str = "linear",
    ):
        risk_limit_info = self.get_risk_limit_info(symbol=symbol, category=category)
        mmr_pct = float(risk_limit_info["maintenanceMargin"])

        return mmr_pct

    def set_position_mode(
        self,
        position_mode: int,
        symbol: str,
        category: str = "linear",
        trading_with: str = None,
    ):
        """
        https://bybit-exchange.github.io/docs/v5/position/position-mode
        """
        end_point = "/v5/position/switch-mode"

        params = {}
        params["category"] = category
        params["symbol"] = symbol
        params["coin"] = trading_with
        params["mode"] = position_mode

        response: dict = self.__HTTP_post_request(end_point=end_point, params=params)
        try:
            if response["retMsg"] in ["OK", "Position mode is not modified"]:
                return True
            else:
                raise Exception
        except Exception as e:
            raise Exception(f"Bybit set_position_mode - {response['retMsg']} -> {e}")

    def get_all_symbols_info(
        self,
        category: str = "linear",
        limit: int = 500,
        symbol: str = None,
        status: str = None,
        baseCoin: str = None,
    ):
        """
        [Bybit API link to Get Instrument Info](https://bybit-exchange.github.io/docs/v5/market/instrument)
        """
        end_point = "/v5/market/instruments-info"

        params = {}
        params["limit"] = limit
        params["category"] = category
        params["symbol"] = symbol
        params["status"] = status
        params["baseCoin"] = baseCoin

        response: dict = get(url=self.url_start + end_point, params=params).json()
        try:
            response["result"]["list"][0]
            data_list = response["result"]["list"]

            return data_list
        except Exception as e:
            raise Exception(f"Bybit get_all_symbols_info = Data or List is empty {response['retMsg']} -> {e}")

    def get_symbols_list(self):
        """
        Returns a list of the symbols in alphabetical order

        Parameters
        ----------
        None

        Returns
        -------
        list
            symbols
        """
        symbols = []
        for info in self.get_all_symbols_info():
            symbols.append(info["symbol"])
            symbols.sort()
        return symbols

    def __get_min_max_leverage_and_asset_size(
        self,
        symbol: str,
    ):
        symbol_info = self.get_all_symbols_info(symbol=symbol)[0]
        max_leverage = float(symbol_info["leverageFilter"]["maxLeverage"])
        min_leverage = float(symbol_info["leverageFilter"]["minLeverage"])
        max_asset_size = float(symbol_info["lotSizeFilter"]["maxOrderQty"])
        min_asset_size = float(symbol_info["lotSizeFilter"]["minOrderQty"])
        asset_tick_step = self.int_value_of_step_size(symbol_info["lotSizeFilter"]["qtyStep"])
        price_tick_step = self.int_value_of_step_size(symbol_info["priceFilter"]["tickSize"])
        leverage_tick_step = self.int_value_of_step_size(symbol_info["leverageFilter"]["leverageStep"])

        return (
            max_leverage,
            min_leverage,
            max_asset_size,
            min_asset_size,
            asset_tick_step,
            price_tick_step,
            leverage_tick_step,
        )

    def get_trading_fee_rates(
        self,
        symbol: str = None,
        baseCoin: str = None,
        category: str = "linear",
    ):
        """
        https://bybit-exchange.github.io/docs/v5/account/fee-rate
        """
        end_point = "/v5/account/fee-rate"

        params = {}
        params["symbol"] = symbol
        params["category"] = category
        params["baseCoin"] = baseCoin

        response: dict = self.__HTTP_get_request(end_point=end_point, params=params)
        try:
            data_list = response["result"]["list"]
            return data_list
        except Exception as e:
            raise Exception(f"bybit get_symbol_trading_fee_rates {response['retMsg']} -> {e}")

    def get_symbol_trading_fee_rates(
        self,
        symbol: str,
        baseCoin: str = None,
        category: str = "linear",
    ):
        trading_fee_rates = self.get_trading_fee_rates(symbol=symbol, baseCoin=baseCoin, category=category)[0]
        return trading_fee_rates

    def get_fee_pcts(
        self,
        symbol: str,
    ):
        trading_fee_info = self.get_symbol_trading_fee_rates(symbol=symbol)
        market_fee_pct = float(trading_fee_info["takerFeeRate"])
        limit_fee_pct = float(trading_fee_info["makerFeeRate"])

        return market_fee_pct, limit_fee_pct

    def set_leverage_mode_cross(self):
        true_false = self.set_leverage_mode(setMarginMode="REGULAR_MARGIN")

        return true_false

    def set_leverage_mode_isolated(self):
        true_false = self.set_leverage_mode(setMarginMode="ISOLATED_MARGIN")

        return true_false

    def set_position_mode_as_hedge_mode(
        self,
        symbol: str,
    ):
        true_false = self.set_position_mode(symbol=symbol, position_mode=3)

        return true_false

    def set_position_mode_as_one_way_mode(
        self,
        symbol: str,
    ):
        true_false = self.set_position_mode(symbol=symbol, position_mode=0)

        return true_false

    def set_and_get_exchange_settings_tuple(
        self,
        leverage_mode: int,
        position_mode: int,
        symbol: str,
    ):
        self.position_mode = position_mode
        if position_mode == PositionModeType.HedgeMode:
            self.set_position_mode_as_hedge_mode(symbol=symbol)
        else:
            self.set_position_mode_as_one_way_mode(symbol=symbol)

        if leverage_mode == LeverageModeType.Isolated:
            self.set_leverage_mode_isolated()
        else:
            self.set_leverage_mode_cross()

        market_fee_pct, limit_fee_pct = self.get_fee_pcts(symbol=symbol)
        (
            max_leverage,
            min_leverage,
            max_asset_size,
            min_asset_size,
            asset_tick_step,
            price_tick_step,
            leverage_tick_step,
        ) = self.__get_min_max_leverage_and_asset_size(symbol=symbol)

        return ExchangeSettings(
            asset_tick_step=asset_tick_step,
            market_fee_pct=market_fee_pct,
            limit_fee_pct=limit_fee_pct,
            mmr_pct=self.__get_mmr_pct(symbol=symbol),
            max_leverage=max_leverage,
            min_leverage=min_leverage,
            max_asset_size=max_asset_size,
            min_asset_size=min_asset_size,
            position_mode=position_mode,
            leverage_mode=leverage_mode,
            price_tick_step=price_tick_step,
            leverage_tick_step=leverage_tick_step,
        )

    def list_of_functions(self):
        func_list = inspect.getmembers(Bybit, predicate=inspect.isfunction)
        new_list = []
        for func in func_list:
            func_name = func[0]
            if not "_" in func_name[0]:
                new_list.append(func[0])
        return new_list

    def close_hedge_positions_and_orders(
        self,
        symbol: str = None,
        settleCoin: str = None,
    ):
        """
        Parameters
        ----------
        symbol : str
        """

        position_info = self.get_position_info(symbol=symbol, settleCoin=settleCoin)

        order_type = "Market"

        asset_size_0 = float(position_info[0]["size"])
        # Return buy or sale based on pos side (if in a short, side == sell)
        if asset_size_0 > 0:
            position_mode = int(position_info[0]["positionIdx"])
            buy_sell = "Sell" if position_mode == 1 else "Buy"
            self.create_order(
                symbol=symbol,
                order_type=order_type,
                asset_size=asset_size_0,
                buy_sell=buy_sell,
                position_mode=position_mode,
            )

        asset_size_1 = float(position_info[1]["size"])
        if asset_size_1 > 0:
            position_mode = int(position_info[1]["positionIdx"])
            buy_sell = "Buy" if position_mode == 2 else "Sell"
            self.create_order(
                symbol=symbol,
                order_type=order_type,
                asset_size=asset_size_1,
                buy_sell=buy_sell,
                position_mode=position_mode,
            )

        self.cancel_all_open_orders_per_symbol(symbol=symbol)

        sleep(1)

        open_order_list = self.get_open_orders(symbol=symbol)

        position_info = self.get_position_info(symbol=symbol)

        asset_size_0 = float(position_info[0]["size"])
        asset_size_1 = float(position_info[1]["size"])

        if open_order_list or asset_size_0 > 0 or asset_size_1 > 0:
            return False
        else:
            return True
