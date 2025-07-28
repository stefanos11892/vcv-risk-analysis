import pytest
import pandas as pd
import numpy as np
from src.data_loader import download_data

def test_download_data_structure():
    prices = download_data(["AAPL"], start="2024-01-01", end="2024-06-30")
    assert isinstance(prices, pd.DataFrame)
    assert not prices.empty
    assert "Adj Close" in prices.columns or "Close" in prices.columns
