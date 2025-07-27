import yfinance as yf
import pandas as pd
from typing import List

def download_prices(tickers: List[str], start: str, end: str) -> pd.DataFrame:
    """Download price data for a list of tickers between start and end dates."""
    data = yf.download(tickers, start=start, end=end, progress=False)
    if 'Adj Close' in data.columns.levels[0]:
        prices = data['Adj Close']
    else:
        prices = data['Close']
    prices.dropna(how='all', axis=1, inplace=True)
    return prices
