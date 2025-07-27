import yfinance as yf
import pandas as pd
from typing import Iterable

def download_data(tickers: Iterable[str], start: str, end: str) -> pd.DataFrame:
    """Download adjusted close prices for one or more tickers."""
    single = isinstance(tickers, str)
    if single:
        tickers = [tickers]

    data = yf.download(list(tickers), start=start, end=end, progress=False)

    if isinstance(data.columns, pd.MultiIndex):
        field = "Adj Close" if "Adj Close" in data.columns.levels[0] else "Close"
        prices = data[field]
    else:
        field = "Adj Close" if "Adj Close" in data.columns else "Close"
        prices = data[[field]].rename(columns={field: tickers[0]})

    prices = prices.dropna(how="all")

    if single:
        prices.columns = ["Close"]

    return prices
