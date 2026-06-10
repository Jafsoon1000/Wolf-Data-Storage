from typing import Iterable

import pandas as pd


def ema(series: pd.Series, period: int) -> pd.Series:
    """Calculate the Exponential Moving Average (EMA) for a pandas Series."""
    return series.ewm(span=period, adjust=False).mean()


def add_standard_emas(df: pd.DataFrame, periods: Iterable[int] = (8, 21, 55)) -> pd.DataFrame:
    """Add standard EMA columns to OHLCV price data."""
    if "close" not in df.columns:
        raise ValueError("DataFrame must contain a 'close' column.")

    output = df.copy()
    for period in periods:
        output[f"ema{period}"] = ema(output["close"], period)
    return output
