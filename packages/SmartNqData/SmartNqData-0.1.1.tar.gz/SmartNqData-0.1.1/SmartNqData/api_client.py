# SmartNqData/api_client.py

import requests
import pandas as pd
from .utils import is_valid_timeframe, format_indicator
from .enums import Timeframe

class SmartNqClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def GetFutureData(self, contract_symbol, start_datetime, end_datetime, timeframe, indicators):
        if not all(is_valid_timeframe(timeframe, indicator_timeframe) for indicator_timeframe in indicators.values()):
            raise ValueError("Indicator timeframe must be less granular than the main requested timeframe.")
        
        formatted_indicators = [format_indicator(ind, tf) for ind, tf in indicators.items()]
        
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
        df = pd.DataFrame(data)

        return df
