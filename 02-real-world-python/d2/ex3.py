from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, ValidationError


class LaxModel(BaseModel):
    """Default (lax) mode: Pydantic coerces when no information is lost."""

    n: int = 0
    flag: bool = False


class StrictModel(BaseModel):
    """Strict mode: inputs must already be the exact type."""

    model_config = ConfigDict(strict=True)

    n: int = 0
    flag: bool = False


CASES: list[dict[str, Any]] = [
    {"n": "42"},
    {"n": 4.0},
    {"n": 4.5},
    {"flag": "yes"},
    {"flag": "maybe"},
    {"flag": 1},
]


def run(model: type[BaseModel]) -> None:
    """Validate every case against the given model and print the outcome."""
    print(f"\n=== {model.__name__} ===")
    for case in CASES:
        try:
            result = model.model_validate(case)
            print(f"  {case!r:<18} -> OK    {result!r}")
        except ValidationError as e:
            print(f"  {case!r:<18} -> ERROR {e.errors()[0]['msg']}")


def main() -> None:
    """Run the same inputs in lax and strict mode."""
    run(LaxModel)
    run(StrictModel)


if __name__ == "__main__":
    main()
