from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest
from pydantic import ValidationError

from d2.ex1 import Signup
from d2.ex2 import Order
from d3.orders import load_orders, report

VALID_SIGNUP: dict[str, Any] = {
    "username": "valid_user",
    "age": 30,
    "password": "securepassword",
    "confirm_password": "securepassword",
}

VALID_ORDERS: list[dict[str, Any]] = [
    {"id": 1, "item": "pen", "qty": 2},
    {"id": 2, "item": "book", "qty": 1},
    {"id": 3, "item": "cup", "qty": 4},
]


# --- 1. Parametrized Signup validation ---


@pytest.mark.parametrize(
    ("data", "expected_loc"),
    [
        pytest.param(
            {**VALID_SIGNUP, "username": "ab"}, ("username",), id="short-username"
        ),
        pytest.param(
            {**VALID_SIGNUP, "username": "bad user!"}, ("username",), id="invalid-chars"
        ),
        pytest.param({**VALID_SIGNUP, "age": 17}, ("age",), id="underage"),
        # model_validator errors belong to the whole model, so loc is empty.
        pytest.param(
            {**VALID_SIGNUP, "confirm_password": "differentpass"},
            (),
            id="password-mismatch",
        ),
    ],
)
def test_invalid_signup_reports_failing_field(
    data: dict[str, Any], expected_loc: tuple[str, ...]
) -> None:
    """Each invalid signup fails on exactly the expected field."""
    with pytest.raises(ValidationError) as exc_info:
        Signup.model_validate(data)

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == expected_loc


def test_valid_signup() -> None:
    """A fully valid signup is accepted unchanged."""
    signup = Signup.model_validate(VALID_SIGNUP)

    assert signup.username == "valid_user"
    assert signup.age == 30


# --- 2. File fixture with tmp_path ---


@pytest.fixture
def orders_file(tmp_path: Path) -> Path:
    """Write three valid orders to a temporary JSON file."""
    path = tmp_path / "orders.json"
    path.write_text(json.dumps(VALID_ORDERS), encoding="utf-8")
    return path


def test_load_orders_reads_all(orders_file: Path) -> None:
    """All three orders in the file are loaded."""
    orders = load_orders(orders_file)

    assert [o.id for o in orders] == [1, 2, 3]


def test_load_orders_points_at_corrupt_index(orders_file: Path) -> None:
    """A corrupt entry is reported with its list index."""
    rows = json.loads(orders_file.read_text(encoding="utf-8"))
    rows.append({"id": 4, "item": "mug", "qty": 0})
    orders_file.write_text(json.dumps(rows), encoding="utf-8")

    with pytest.raises(ValidationError) as exc_info:
        load_orders(orders_file)

    errors = exc_info.value.errors()
    assert len(errors) == 1
    assert errors[0]["loc"] == (3, "qty")


# --- 3. Capturing output with capsys ---


def test_report_prints_lines_and_total(capsys: pytest.CaptureFixture[str]) -> None:
    """report prints one line per order and a total quantity line."""
    orders = [Order.model_validate(row) for row in VALID_ORDERS]

    report(orders)

    out = capsys.readouterr().out
    assert out.splitlines() == [
        "#1 pen x2",
        "#2 book x1",
        "#3 cup x4",
        "Total qty: 7",
    ]
