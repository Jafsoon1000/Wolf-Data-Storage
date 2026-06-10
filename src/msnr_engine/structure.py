from typing import Dict, Optional

import pandas as pd


def detect_trend(df: pd.DataFrame) -> str:
    """Return a simple trend signal from EMA alignment."""
    required_columns = {"ema8", "ema21", "ema55"}
    if not required_columns.issubset(df.columns):
        raise ValueError("DataFrame must contain ema8, ema21, and ema55 columns.")
    if len(df) < 1:
        return "flat"

    latest = df.iloc[-1]
    if latest["ema8"] > latest["ema21"] > latest["ema55"]:
        return "bullish"
    if latest["ema8"] < latest["ema21"] < latest["ema55"]:
        return "bearish"
    return "flat"


def detect_break_of_structure(df: pd.DataFrame) -> Optional[Dict[str, object]]:
    """Detect a simple bullish or bearish break of structure."""
    if len(df) < 6:
        return None

    window = df.iloc[-6:]
    high_series = window["high"]
    low_series = window["low"]
    current = window.iloc[-1]
    prior_high = high_series.iloc[:-1].max()
    prior_low = low_series.iloc[:-1].min()

    if current["high"] > prior_high and current["close"] > window["ema21"].iloc[-1]:
        return {
            "type": "bullish",
            "break_level": prior_high,
            "trigger_price": current["high"],
        }

    if current["low"] < prior_low and current["close"] < window["ema21"].iloc[-1]:
        return {
            "type": "bearish",
            "break_level": prior_low,
            "trigger_price": current["low"],
        }

    return None
