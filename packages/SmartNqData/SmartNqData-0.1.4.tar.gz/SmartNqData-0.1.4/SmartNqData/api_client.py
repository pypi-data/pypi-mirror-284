# SmartNqData/api_client.py

import requests
import pandas as pd
from datetime import datetime
import pytz
from .utils import is_valid_timeframe, format_indicator
from .enums import Timeframe

class SmartNqClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.est = pytz.timezone('US/Eastern')

    def GetFutureData(self, contract_symbol, start_datetime, end_datetime, timeframe, indicators):
        if not all(is_valid_timeframe(timeframe, indicator_timeframe) for indicator_timeframe in indicators.values()):
            raise ValueError("Indicator timeframe must be less granular than the main requested timeframe.")
        
        formatted_indicators = [format_indicator(ind, tf, timeframe) for ind, tf in indicators.items()]
        
        payload = {
            "contractSymbol": contract_symbol,
            "startDateTime": start_datetime,
            "endDateTime": end_datetime,
            "timeframe": timeframe.value,
            "requestedIndicators": formatted_indicators
        }

        response = requests.post(f'{self.base_url}/api/Data/query', json=payload)
        response.raise_for_status()

        data = response.json()
        
        candles = data['candles']
        formatted_data = []

        for candle in candles:
            row = {
                'Time': datetime.fromtimestamp(candle['t'], self.est),
                'Open': candle['o'],
                'High': candle['h'],
                'Low': candle['l'],
                'Close': candle['c'],
                'Volume': candle['v']
            }
            row.update(candle['i'])
            formatted_data.append(row)

        df = pd.DataFrame(formatted_data)

        return df
