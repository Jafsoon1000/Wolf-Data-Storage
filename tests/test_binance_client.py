import pytest

from src.data_ingestion.binance_client import BinanceOHLCVClient


def test_binance_client_requires_credentials(monkeypatch):
    monkeypatch.delenv("BINANCE_API_KEY", raising=False)
    monkeypatch.delenv("BINANCE_API_SECRET", raising=False)
    with pytest.raises(ValueError):
        BinanceOHLCVClient()
