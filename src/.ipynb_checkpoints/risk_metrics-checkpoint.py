import numpy as np
import pandas as pd
from typing import Tuple

def compute_var(returns: pd.Series, alpha: float = 0.95) -> float:
    """Compute historical Value at Risk."""
    return np.percentile(returns, (1 - alpha) * 100)

def compute_cvar(returns: pd.Series, alpha: float = 0.95) -> float:
    """Compute Conditional Value at Risk."""
    var = compute_var(returns, alpha)
    return returns[returns <= var].mean()

def portfolio_returns(prices: pd.DataFrame, weights: np.ndarray) -> pd.Series:
    """Calculate portfolio returns from price data and weights."""
    log_returns = np.log(prices / prices.shift(1)).dropna()
    return log_returns @ weights
