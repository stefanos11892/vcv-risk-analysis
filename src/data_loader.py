import yfinance as yf
import pandas as pd
from typing import Iterable

def download_data(
    tickers: Iterable[str], start: str, end: str, field: str = "Adj Close"
) -> pd.DataFrame:
    """Download price data for one or more tickers.

    Parameters
    ----------
    tickers : Iterable[str] or str
        Symbols to download.
    start, end : str
        Date range for the download.
    field : str, default "Adj Close"
        Which price field to return (falls back to ``"Close"`` if unavailable).
    """

    single = isinstance(tickers, str)
    tickers_list = [tickers] if single else list(tickers)

    data = yf.download(tickers_list, start=start, end=end, progress=False)

    if isinstance(data.columns, pd.MultiIndex):
        use_field = field if field in data.columns.levels[0] else "Close"
        prices = data[use_field]
    else:
        use_field = field if field in data.columns else "Close"
        prices = data[[use_field]].rename(columns={use_field: tickers_list[0]})

    prices = prices.dropna(how="all")

    if single:
        prices.columns = ["Close"]

    return prices
