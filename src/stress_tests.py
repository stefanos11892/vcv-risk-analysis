import numpy as np
import pandas as pd
from typing import List, Optional
from .data_loader import download_data
from .risk_metrics import portfolio_returns

def historical_stress_test(
    tickers: List[str],
    weights: np.ndarray,
    start: str,
    end: str,
    field: str = "Adj Close",
    label: Optional[str] = None,
    local_path: Optional[str] = None
) -> pd.Series:
    """
    Return cumulative portfolio return for historical period.
    Optionally labels the output series.
    """
    prices = download_data(tickers, start, end, field=field, local_path=local_path)

    if len(weights) != len(prices.columns):
        raise ValueError("Length of weights must match number of tickers.")

    weights = np.array(weights)
    weights /= weights.sum()  # Normalize

    port_ret = portfolio_returns(prices, weights)
    result = (1 + port_ret).cumprod()

    if label:
        result.name = label

    return result
