import json
from dataclasses import dataclass
from typing import NotRequired, TypedDict


@dataclass
class Todo:
    """A to-do item as the rest of the code sees it (the domain object)."""

    title: str
    done: bool = False
    due: str | None = None


class TodoDict(TypedDict):
    """The JSON shape of one to-do (only a type; at runtime it's a plain dict)."""

    title: str
    done: bool
    due: NotRequired[str]  # The key may be missing entirely.


def to_dict(todo: Todo) -> TodoDict:
    """Convert a Todo into a dict ready for json.dump."""
    d: TodoDict = {"title": todo.title, "done": todo.done}
    if todo.due is not None:
        d["due"] = todo.due
    return d


def from_dict(d: TodoDict) -> Todo:
    """Build a Todo from a dict loaded from JSON."""
    return Todo(title=d["title"], done=d["done"], due=d.get("due"))


def main() -> None:
    todos = [Todo("Learn TypedDict"), Todo("Week 2 review", due="2026-10-09")]

    text = json.dumps([to_dict(t) for t in todos], indent=2)
    print(text)

    # json.loads returns Any: the annotation tells mypy the shape, but nothing checks it at runtime.
    loaded: list[TodoDict] = json.loads(text)
    print([from_dict(d) for d in loaded])


if __name__ == "__main__":
    main()
