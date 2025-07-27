import numpy as np
import pandas as pd
from typing import List, Tuple
from .data_loader import download_data
from .risk_metrics import portfolio_returns


def historical_stress_test(
    tickers: List[str],
    weights: np.ndarray,
    start: str,
    end: str,
    label: str,
) -> pd.Series:
    """Return cumulative portfolio return for historical period."""
    prices = download_data(tickers, start, end)
    weights = np.array(weights)[: len(prices.columns)]
    weights = weights / weights.sum()
    port_ret = portfolio_returns(prices, weights)
    return (1 + port_ret).cumprod()
