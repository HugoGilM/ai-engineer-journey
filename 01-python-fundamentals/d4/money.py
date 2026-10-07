from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal


@dataclass(frozen=True)
class Money:
    """An immutable amount of money in a given currency."""

    amount: Decimal
    currency: str

    def add(self, other: Money) -> Money:
        """Return a new Money with the summed amount; currencies must match."""
        if self.currency != other.currency:
            raise ValueError(f"cannot add {other.currency} to {self.currency}")
        return Money(self.amount + other.amount, self.currency)

    def __add__(self, other: object) -> Money:
        """Enable `m1 + m2`; non-Money operands get a clean TypeError."""
        if not isinstance(other, Money):
            return NotImplemented
        return self.add(other)


if __name__ == "__main__":
    a = Money(Decimal("10.50"), "EUR")
    b = Money(Decimal("0.20"), "EUR")
    total = a.add(b)
    print(total)
    print("originals unchanged:", a, b)
    print("with +:", a + b)

    try:
        a + 5
    except TypeError as e:
        print("TypeError:", e)

    try:
        a.add(Money(Decimal("5.0"), "USD"))
    except ValueError as e:
        print("ValueError:", e)

    try:
        a.amount = Decimal("999")
    except AttributeError as e:  # FrozenInstanceError subclasses AttributeError.
        print(type(e).__name__ + ":", e)

    print(
        "equal by value:",
        Money(Decimal("1.00"), "EUR") == Money(Decimal("1.00"), "EUR"),
    )
