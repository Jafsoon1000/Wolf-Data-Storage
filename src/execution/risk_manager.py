from typing import Optional


def calculate_risk_per_trade(account_balance: float, risk_percentage: float) -> float:
    """Calculate the dollar risk for a trade based on account size and risk percentage."""
    if account_balance <= 0:
        raise ValueError("Account balance must be positive.")
    if not (0 < risk_percentage <= 1):
        raise ValueError("Risk percentage must be a decimal value between 0 and 1.")
    return account_balance * risk_percentage


def calculate_position_size(
    account_balance: float,
    risk_percentage: float,
    stop_loss_distance: float,
    entry_price: float,
) -> float:
    """Calculate trade size based on risk amount and stop-loss distance."""
    risk_amount = calculate_risk_per_trade(account_balance, risk_percentage)
    if stop_loss_distance <= 0:
        raise ValueError("Stop-loss distance must be greater than zero.")
    if entry_price <= 0:
        raise ValueError("Entry price must be greater than zero.")
    quantity = risk_amount / stop_loss_distance
    return round(quantity, 8)
