import os
import yfinance as yf
import pandas as pd
from typing import Iterable, Optional

def download_data(
    tickers: Iterable[str],
    start: str,
    end: str,
    field: str = "adjClose",
    local_path: Optional[str] = None,
) -> pd.DataFrame:
    """
    Download price data for one or more tickers.

    Parameters:
    tickers : Iterable[str] or str
        Symbols to download.
    start, end : str
        Date range for the download.
    field : str, default "adjClose"
        Which price field to return (falls back to "Close" if unavailable).
    local_path : str, optional
        If provided, data will be loaded from this CSV if it exists. If the
        online request fails and a file is available, it is used as a fallback.
        Otherwise downloaded data will be saved to this path for future use.

    Returns:
    -------
    pd.DataFrame with prices.
    """
    single = isinstance(tickers, str)
    tickers_list = [tickers] if single else list(tickers)

    if local_path:
        all_data = []
        for ticker in tickers_list:
            file_path = os.path.join(local_path, f"{ticker}_data.csv")
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Expected file not found: {file_path}")
            df = pd.read_csv(file_path, index_col="date", parse_dates=True)
            df = df[['adjClose']].rename(columns={'adjClose': ticker})
            all_data.append(df)
        data = pd.concat(all_data, axis=1)
    else:
        data = yf.download(tickers_list, start=start, end=end, progress=False)

        # Extract field from multi-index or fallback
        if isinstance(data.columns, pd.MultiIndex):
            use_field = field if field in data.columns.levels[0] else "Close"
            prices = data[use_field]
        else:
            use_field = field if field in data.columns else "Close"
            prices = data[[use_field]].rename(columns={use_field: tickers_list[0]})
        prices = prices.dropna(how="all")
        if prices.empty:
            raise ValueError("No price data available. The download may have failed or returned empty results.")
        if single:
            prices.columns = ["Close"]
        return prices

    if data.empty:
        raise ValueError("No price data available. Your local CSVs might be empty or corrupted.")

    return data
