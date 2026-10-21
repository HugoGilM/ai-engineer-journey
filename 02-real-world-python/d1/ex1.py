from collections.abc import Iterable


def parse_price(raw: str) -> None | float:
    if raw.strip() == "":
        return None
    return float(raw)


def total(prices: Iterable[float]) -> float:
    return sum(prices)


def apply_discount(prices: Iterable[float], pct: float) -> list[float]:
    return [p * (1 - pct / 100) for p in prices]


parsed = [parse_price(s) for s in ["10.5", "", "3"]]
prices = [p for p in parsed if p is not None]
print(total(apply_discount(prices, 10)))
