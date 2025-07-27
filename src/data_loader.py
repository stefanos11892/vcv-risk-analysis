import yfinance as yf
import pandas as pd
from typing import Iterable

def download_data(tickers: Iterable[str], start: str, end: str) -> pd.DataFrame:
    """Download price data for one or more tickers."""
    if isinstance(tickers, str):
        tickers = [tickers]
    data = yf.download(list(tickers), start=start, end=end, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        field = 'Adj Close' if 'Adj Close' in data.columns.levels[0] else 'Close'
        prices = data[field]
    else:
        field = 'Adj Close' if 'Adj Close' in data.columns else 'Close'
        prices = data[field].to_frame(tickers[0])
    prices.dropna(how='all', axis=1, inplace=True)
    return prices
