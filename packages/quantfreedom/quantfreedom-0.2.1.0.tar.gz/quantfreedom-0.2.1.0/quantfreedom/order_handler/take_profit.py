import numpy as np

from logging import getLogger

from quantfreedom.helpers.helper_funcs import round_size_by_tick_step
from quantfreedom.core.enums import (
    CandleBodyType,
    CurrentFootprintCandleTuple,
    DecreasePosition,
    OrderStatus,
    TakeProfitStrategyType,
)

logger = getLogger()


class TakeProfit:
    risk_reward: float

    def __init__(
        self,
        long_short: str,
        market_fee_pct: float,
        price_tick_step: float,
        tp_fee_pct: float,
        tp_strategy_type: TakeProfitStrategyType,  # type: ignore
    ):
        self.market_fee_pct = market_fee_pct
        self.price_tick_step = price_tick_step
        self.tp_fee_pct = tp_fee_pct

        if long_short.lower() == "long":
            self.get_tp_price = self.long_tp_price
            self.get_check_tp_candle_price = self.long_c_tp_candle
        elif long_short.lower() == "short":
            self.get_tp_price = self.short_tp_price
            self.get_check_tp_candle_price = self.short_c_tp_candle
        else:
            raise Exception("long or short are the only options for long_short")

        if tp_strategy_type == TakeProfitStrategyType.RiskReward:
            self.tp_calculator = self.tp_rr
            self.checker_tp_hit = self.c_tp_hit_regular
        if tp_strategy_type == TakeProfitStrategyType.Provided:
            self.tp_calculator = self.tp_provided
            self.checker_tp_hit = self.c_tp_hit_provided
        if tp_strategy_type == TakeProfitStrategyType.Nothing:
            self.tp_calculator = self.tp_provided
            self.checker_tp_hit = self.c_tp_hit_nothing

    def short_tp_price(
        self,
        average_entry: float,
        position_size_usd: float,
        profit: float,
    ):
        tp_price = -(
            (profit * average_entry)
            - (average_entry * position_size_usd)
            + (average_entry * self.market_fee_pct * position_size_usd)
        ) / (position_size_usd * (1 + self.tp_fee_pct))
        return tp_price

    def short_c_tp_candle(
        self,
        current_candle: CurrentFootprintCandleTuple,
        tp_price: float,
    ):
        candle_low = current_candle[CandleBodyType.Low]
        logger.debug(f"candle_high= {candle_low}")
        return tp_price > candle_low

    def long_tp_price(
        self,
        average_entry: float,
        position_size_usd: float,
        profit: float,
    ):
        tp_price = (
            (profit * average_entry)
            + (average_entry * position_size_usd)
            + (average_entry * self.market_fee_pct * position_size_usd)
        ) / (position_size_usd * (1 - self.tp_fee_pct))
        return tp_price

    def long_c_tp_candle(
        self,
        current_candle: CurrentFootprintCandleTuple,
        tp_price: float,
    ):
        candle_high = current_candle[CandleBodyType.High]
        logger.debug(f"candle_high= {candle_high}")
        result = tp_price < candle_high
        return result

    def tp_rr(
        self,
        average_entry: float,
        position_size_usd: float,
        total_possible_loss: float,
    ):
        profit = -total_possible_loss * self.risk_reward
        logger.debug(f"possible profit= {profit}")
        tp_price = self.get_tp_price(
            average_entry=average_entry,
            position_size_usd=position_size_usd,
            profit=profit,
        )

        tp_price = round_size_by_tick_step(
            user_num=tp_price,
            exchange_num=self.price_tick_step,
        )
        logger.debug(f"tp_price= {tp_price}")

        tp_pct = round(abs((tp_price - average_entry)) / average_entry, 2)
        logger.debug(f"tp_pct= {round(tp_pct * 100, 2)}")
        can_move_sl_to_be = True
        logger.debug("can_move_sl_to_be= True")
        return (
            can_move_sl_to_be,
            tp_price,
            tp_pct,
        )

    def tp_provided(
        self,
        average_entry: float,
        position_size_usd: float,
        total_possible_loss: float,
    ):
        can_move_sl_to_be = True
        tp_price = np.nan
        tp_pct = np.nan

        return (
            can_move_sl_to_be,
            tp_price,
            tp_pct,
        )

    def c_tp_hit_regular(
        self,
        current_candle: CurrentFootprintCandleTuple,
        exit_price: float,
        tp_price: float,
    ):
        if self.get_check_tp_candle_price(
            current_candle=current_candle,
            tp_price=tp_price,
        ):
            logger.debug(f"TP Hit tp_price= {tp_price}")
            raise DecreasePosition(
                exit_fee_pct=self.tp_fee_pct,
                exit_price=tp_price,
                order_status=OrderStatus.TakeProfitFilled,
            )
        else:
            logger.debug("No Tp Hit")
            pass

    def c_tp_hit_nothing(
        self,
        current_candle: CurrentFootprintCandleTuple,
        exit_price: float,
        tp_price: float,
    ):
        pass

    def c_tp_hit_provided(
        self,
        current_candle: CurrentFootprintCandleTuple,
        exit_price: float,
        tp_price: float,
    ):
        if not np.isnan(exit_price):
            logger.debug(f"TP Hit tp_price= {exit_price}")
            raise DecreasePosition(
                exit_fee_pct=self.tp_fee_pct,
                exit_price=exit_price,
                order_status=OrderStatus.TakeProfitFilled,
            )
        else:
            logger.debug("No Tp Hit")
            pass
