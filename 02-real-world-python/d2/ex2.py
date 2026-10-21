from __future__ import annotations

import json

from pydantic import BaseModel, Field, TypeAdapter, ValidationError


class Order(BaseModel):
    """A single order line."""

    id: int
    item: str
    qty: int = Field(gt=0)


RAW = '[{"id": 1, "item": "pen", "qty": 2}, {"id": 2, "item": "book", "qty": 1}, {"id": "x", "item": "cup", "qty": 1}]'


def main() -> None:
    """Parse the orders and report exactly which rows failed and why."""
    adapter: TypeAdapter[list[Order]] = TypeAdapter(list[Order])
    try:
        orders = adapter.validate_json(RAW)
        print(orders)
    except ValidationError as e:
        rows = json.loads(RAW)
        print(f"{e.error_count()} error(s):")
        for err in e.errors():
            index, field = err["loc"][0], err["loc"][1]
            assert isinstance(index, int)
            print(
                f"  row {index} ({rows[index]}): "
                f"field '{field}' = {err['input']!r} -> {err['msg']}"
            )


if __name__ == "__main__":
    main()
