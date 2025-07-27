# Suggested Repository Structure

This repository currently contains a single Jupyter notebook. To enable easier
development and extension of VaR/CVaR and stress testing functionality, the
following lightweight Python package is proposed.

```
vcv-risk-analysis/
├── src/
│   ├── __init__.py
│   ├── data_loader.py      # Download and clean market data
│   ├── risk_metrics.py     # VaR, CVaR and portfolio return utilities
│   └── stress_tests.py     # Historical/hypothetical stress test helpers
└── VCV Risk Analysis Test A.ipynb
```

Each module exposes simple functions which can be imported into notebooks or
other scripts. Future work can add unit tests under a `tests/` folder and CLI
interfaces or dashboards. Splitting logic this way keeps notebooks lean and
improves reusability.
