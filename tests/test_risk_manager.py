import pytest

from src.execution.risk_manager import calculate_position_size, calculate_risk_per_trade


def test_calculate_risk_per_trade_returns_expected_amount():
    assert calculate_risk_per_trade(10000, 0.01) == 100.0


def test_calculate_position_size_rounds_to_eight_places():
    quantity = calculate_position_size(10000, 0.01, 50, 200)
    assert quantity == 2.0


def test_calculate_position_size_invalid_values_raise():
    with pytest.raises(ValueError):
        calculate_position_size(10000, 0.01, 0, 200)
    with pytest.raises(ValueError):
        calculate_position_size(10000, 0.01, 50, 0)
