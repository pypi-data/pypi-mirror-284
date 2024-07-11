# SmartNqData/utils.py

from .enums import Timeframe

TIMEFRAME_ORDER = [
    Timeframe.MINUTE,
    Timeframe.FIVE_MINUTES,
    Timeframe.TEN_MINUTES,
    Timeframe.FIFTEEN_MINUTES,
    Timeframe.THIRTY_MINUTES,
    Timeframe.HOUR,
    Timeframe.FOUR_HOURS,
    Timeframe.DAILY,
]

def is_valid_timeframe(indicator_timeframe, main_timeframe):
    return TIMEFRAME_ORDER.index(indicator_timeframe) <= TIMEFRAME_ORDER.index(main_timeframe)

def format_indicator(indicator, indicator_timeframe, main_timeframe):
    if indicator_timeframe == main_timeframe:
        return indicator.name
    return f"{indicator_timeframe.value}{indicator.name}"
