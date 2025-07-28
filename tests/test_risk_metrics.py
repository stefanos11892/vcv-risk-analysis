import numpy as np
import pandas as pd
from src.stress_tests import historical_stress_test

def test_stress_test_output_shape():
    tickers = ["AAPL", "MSFT"]
    weights = np.array([0.5, 0.5])
    result = historical_stress_test(tickers, weights, start="2024-01-01", end="2024-06-30")
    assert isinstance(result, pd.Series)
    assert result.notnull().all()
