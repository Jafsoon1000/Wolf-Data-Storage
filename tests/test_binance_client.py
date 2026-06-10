import pytest

from src.data_ingestion.binance_client import BinanceOHLCVClient


def test_binance_client_requires_credentials(monkeypatch):
    import config.settings as settings

    monkeypatch.setattr(settings.BINANCE, "api_key", None)
    monkeypatch.setattr(settings.BINANCE, "api_secret", None)

    with pytest.raises(ValueError):
        BinanceOHLCVClient()
