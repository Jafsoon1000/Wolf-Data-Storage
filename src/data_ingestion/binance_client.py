from datetime import datetime
from typing import List, Optional, Literal

import pandas as pd
from binance.client import Client

from config.settings import BINANCE

Interval = Literal[
    "1m", "3m", "5m", "15m", "30m", "1h", "2h", "4h", "6h", "8h", "12h", "1d", "3d", "1w", "1M"
]


class BinanceOHLCVClient:
    """Simple Binance OHLCV loader for analysis and backtesting."""

    def __init__(
        self,
        api_key: Optional[str] = None,
        api_secret: Optional[str] = None,
        testnet: bool = False,
    ):
        self.api_key = api_key or BINANCE_API_KEY
        self.api_secret = api_secret or BINANCE_API_SECRET
        if not self.api_key or not self.api_secret:
            raise ValueError("Binance API credentials are required to initialize the client.")

        self.client = Client(self.api_key, self.api_secret, testnet=testnet)

    def fetch_historical_klines(
        self,
        symbol: str,
        interval: Interval = "1h",
        start_str: str = "1 month ago UTC",
        end_str: Optional[str] = None,
        limit: int = 1000,
    ) -> pd.DataFrame:
        """Fetch historical klines from Binance and return a cleaned DataFrame."""
        klines = self.client.get_historical_klines(
            symbol=symbol,
            interval=interval,
            start_str=start_str,
            end_str=end_str,
            limit=limit,
        )

        if not klines:
            return pd.DataFrame()

        df = pd.DataFrame(
            klines,
            columns=[
                "open_time",
                "open",
                "high",
                "low",
                "close",
                "volume",
                "close_time",
                "quote_asset_volume",
                "number_of_trades",
                "taker_buy_base_asset_volume",
                "taker_buy_quote_asset_volume",
                "ignore",
            ],
        )
        df["open_time"] = pd.to_datetime(df["open_time"], unit="ms")
        df["close_time"] = pd.to_datetime(df["close_time"], unit="ms")
        numeric_columns = ["open", "high", "low", "close", "volume"]
        df[numeric_columns] = df[numeric_columns].astype(float)
        return df[["open_time", "open", "high", "low", "close", "volume", "close_time"]]

    def get_historical_ohlcv(
        self,
        symbol: str,
        interval: Interval = "1h",
        start_time: Optional[datetime] = None,
        end_time: Optional[datetime] = None,
        limit: int = 1000,
    ) -> pd.DataFrame:
        """Return historical OHLCV data for a given symbol and time range."""
        start_str = start_time.strftime("%Y-%m-%d %H:%M:%S") if start_time else "1 month ago UTC"
        end_str = end_time.strftime("%Y-%m-%d %H:%M:%S") if end_time else None
        return self.fetch_historical_klines(
            symbol=symbol,
            interval=interval,
            start_str=start_str,
            end_str=end_str,
            limit=limit,
        )
