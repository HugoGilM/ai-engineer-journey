from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from decimal import Decimal


class BankError(Exception):
    """Base class for every banking error, so callers can catch them all at once."""


class InvalidAmountError(BankError):
    """Raised when an amount is zero or negative."""


class InsufficientFundsError(BankError):
    """Raised when a withdrawal asks for more than the available balance."""

    def __init__(self, balance: Decimal, requested: Decimal) -> None:
        self.balance = balance
        self.requested = requested
        super().__init__(f"insufficient funds: balance {balance}, requested {requested}")


@dataclass(frozen=True)
class Transaction:
    kind: str
    amount: Decimal
    timestamp: datetime = field(default_factory=datetime.now)  # Called once per instance.


class BankAccount:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self._balance = Decimal("0")
        self.transactions: list[Transaction] = []

    @property
    def balance(self) -> Decimal:
        return self._balance

    def deposit(self, amount: Decimal, kind: str = "deposit") -> None:
        self._validate(amount)
        self._balance += amount
        self.transactions.append(Transaction(kind, amount))

    def withdraw(self, amount: Decimal, kind: str = "withdraw") -> None:
        self._validate(amount)
        if amount > self._balance:
            raise InsufficientFundsError(self._balance, amount)
        self._balance -= amount
        self.transactions.append(Transaction(kind, amount))

    def transfer_to(self, other: BankAccount, amount: Decimal) -> None:
        """Move money to another account; nothing changes if the withdrawal fails."""
        if other is self:
            raise BankError("cannot transfer to the same account")
        # Withdraw first: if it raises, the deposit never happens. Once it succeeds,
        # the deposit can't fail because the amount was already validated.
        self.withdraw(amount, kind=f"transfer to {other.owner}")
        other.deposit(amount, kind=f"transfer from {self.owner}")

    def statement(self) -> str:
        lines = [f"Statement for {self.owner}"]
        for t in self.transactions:
            lines.append(f"  {t.timestamp:%Y-%m-%d %H:%M:%S}  {t.kind:<22} {t.amount:>10}")
        lines.append(f"  {'balance':<43} {self._balance:>10}")
        return "\n".join(lines)

    @staticmethod
    def _validate(amount: Decimal) -> None:
        if amount <= 0:
            raise InvalidAmountError(f"amount must be positive, got {amount}")

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance})"


def main() -> None:
    alice = BankAccount("Alice")
    bob = BankAccount("Bob")

    alice.deposit(Decimal("100.00"))
    alice.withdraw(Decimal("30.50"))
    alice.transfer_to(bob, Decimal("20.00"))
    bob.deposit(Decimal("5.25"))
    print(alice, bob, sep="\n")

    try:
        alice.deposit(Decimal("-10"))
    except InvalidAmountError as e:
        print("InvalidAmountError:", e)

    try:
        bob.withdraw(Decimal("1000"))
    except InsufficientFundsError as e:
        print(f"InsufficientFundsError: {e} (balance={e.balance}, requested={e.requested})")

    # A failed transfer must leave both balances untouched.
    before = (alice.balance, bob.balance)
    try:
        alice.transfer_to(bob, Decimal("500"))
    except BankError as e:  # The base class catches any banking error.
        print(f"{type(e).__name__}: {e}")
    assert (alice.balance, bob.balance) == before
    print("balances unchanged after failed transfer:", alice.balance, bob.balance)

    print()
    print(alice.statement())
    print()
    print(bob.statement())


if __name__ == "__main__":
    main()
