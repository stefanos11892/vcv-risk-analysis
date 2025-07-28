import os
import pandas as pd
import yfinance as yf
from typing import Iterable, Optional

def download_data(
    tickers: Iterable[str],
    start: str,
    end: str,
    field: str = "Adj Close",  # Yahoo uses space
    local_path: Optional[str] = None,
) -> pd.DataFrame:
    """
    Download or load price data for one or more tickers.
    """

    single = isinstance(tickers, str)
    tickers_list = [tickers] if single else list(tickers)

    all_data = []

    if local_path:
        for ticker in tickers_list:
            file_path = os.path.join(local_path, f"{ticker}_data.csv")
            if not os.path.exists(file_path):
                raise FileNotFoundError(f"Local CSV not found: {file_path}")
            df = pd.read_csv(file_path, index_col="date", parse_dates=True)
            df = df[[field]].rename(columns={field: ticker})
            all_data.append(df)
        prices = pd.concat(all_data, axis=1)
    else:
        try:
            data = yf.download(tickers_list, start=start, end=end, progress=False)
        except Exception as e:
            raise ConnectionError(f"Failed to download from Yahoo: {e}")

        if isinstance(data.columns, pd.MultiIndex):
            use_field = field if field in data.columns.levels[0] else "Close"
            prices = data[use_field]
        else:
            use_field = field if field in data.columns else "Close"
            prices = data[[use_field]].rename(columns={use_field: tickers_list[0]})

        if prices.empty:
            raise ValueError("No price data found. Check ticker symbols or date range.")

        if isinstance(prices, pd.Series):
            prices = prices.to_frame()

        if single:
            prices.columns = [tickers]

    return prices
