import numpy as np
import pandas as pd
from typing import Tuple

def compute_var(returns: pd.Series, confidence_level: float = 0.95) -> float:
    """Compute historical Value at Risk."""
    returns = returns.dropna()
    return np.percentile(returns, (1 - confidence_level) * 100)

def compute_cvar(returns: pd.Series, confidence_level: float = 0.95) -> float:
    """Compute Conditional Value at Risk."""
    returns = returns.dropna()
    var = compute_var(returns, confidence_level=confidence_level)
    return returns[returns <= var].mean()

def portfolio_returns(prices: pd.DataFrame, weights: np.ndarray) -> pd.Series:
    """Calculate portfolio returns from price data and weights."""
    log_returns = np.log(prices / prices.shift(1)).dropna()
    return log_returns @ weights
