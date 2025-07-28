import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import numpy as np
import pandas as pd
from src.stress_tests import historical_stress_test

def test_stress_test_output_shape():
    local_path = r"C:\Users\Michailides\projects\VCVRiskAnalysis\csv"
    tickers = ["AMD", "MSFT"]
    weights = np.array([0.5, 0.5])
    
    result = historical_stress_test(
        tickers,
        weights,
        start="2024-01-01",
        end="2024-06-30",
        local_path=local_path,
        field="adjClose"  # <-- FIXED FIELD NAME HERE
    )

    assert isinstance(result, pd.Series)
    assert result.notnull().all()
