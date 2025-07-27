import os
import yfinance as yf
import pandas as pd
from typing import Iterable, Optional

def download_data(
    tickers: Iterable[str],
    start: str,
    end: str,
    field: str = "Adj Close",
    local_path: Optional[str] = None,
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
    local_path : str, optional
        If provided, data will be loaded from this CSV if it exists. Otherwise
        downloaded data will be saved to this path for future use.
    """

    single = isinstance(tickers, str)
    tickers_list = [tickers] if single else list(tickers)

    if local_path and os.path.exists(local_path):
        data = pd.read_csv(local_path, index_col=0, header=[0, 1], parse_dates=True)
    else:
        data = yf.download(tickers_list, start=start, end=end, progress=False)
        if local_path:
            data.to_csv(local_path)

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
