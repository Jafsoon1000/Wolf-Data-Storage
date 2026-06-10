import pandas as pd

from src.msnr_engine.indicators import add_standard_emas, ema


def test_ema_computes_expected_values():
    series = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])
    result = ema(series, 3)
    assert len(result) == 5
    assert result.iloc[-1] > result.iloc[-2]


def test_add_standard_emas_appends_columns():
    df = pd.DataFrame({"close": [10.0, 12.0, 11.0, 13.0, 15.0]})
    output = add_standard_emas(df)
    assert "ema8" in output.columns
    assert "ema21" in output.columns
    assert "ema55" in output.columns
    assert output["ema8"].iloc[-1] > 0
