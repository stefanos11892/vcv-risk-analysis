# VCV Risk Analysis

This repository contains Python modules for basic risk analysis including Value at Risk (VaR), Conditional Value at Risk (CVaR) and simple stress test utilities. The code is organized as a lightweight package under `src/` for easy re-use in notebooks or other scripts.

## Structure

- **src/data_loader.py** – Functions for downloading market data from yfinance or loading from local CSV files.
- **src/risk_metrics.py** – Helpers to compute VaR, CVaR and portfolio returns.
- **src/stress_tests.py** – Utilities for running historical stress tests on a portfolio.
- **ARCHITECTURE.md** – Outlines the overall package organization.

Example usage:

```python
from src import download_data, compute_var

prices = download_data(["AAPL"], start="2024-01-01", end="2024-06-30")
var = compute_var(prices["Close"].pct_change().dropna())
print("VaR:", var)
```

The repository currently contains several exploratory notebooks and sample CSV files used during development. These are not required for using the package but kept for reference.

