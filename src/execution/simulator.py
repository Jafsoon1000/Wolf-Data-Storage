from typing import Dict


def create_market_order(
    symbol: str,
    side: str,
    quantity: float,
    entry_price: float,
    stop_loss: float,
    take_profit: float,
) -> Dict[str, object]:
    """Build a simulated market order request dictionary."""
    if side not in {"BUY", "SELL"}:
        raise ValueError("side must be either 'BUY' or 'SELL'.")
    return {
        "symbol": symbol,
        "side": side,
        "quantity": round(quantity, 8),
        "entry_price": entry_price,
        "stop_loss": stop_loss,
        "take_profit": take_profit,
        "status": "simulated",
    }
