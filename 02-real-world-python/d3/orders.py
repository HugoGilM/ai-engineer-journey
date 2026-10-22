from __future__ import annotations

from pathlib import Path

from pydantic import TypeAdapter

from d2.ex2 import Order

ORDERS_ADAPTER: TypeAdapter[list[Order]] = TypeAdapter(list[Order])


def load_orders(path: Path) -> list[Order]:
    """Read a JSON array of orders from a file and validate it."""
    return ORDERS_ADAPTER.validate_json(path.read_text(encoding="utf-8"))


def report(orders: list[Order]) -> None:
    """Print one line per order followed by the total quantity."""
    for order in orders:
        print(f"#{order.id} {order.item} x{order.qty}")
    print(f"Total qty: {sum(order.qty for order in orders)}")
