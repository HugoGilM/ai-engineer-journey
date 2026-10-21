from collections.abc import Callable, Iterable


def first_or_default[T](items: Iterable[T], default: T) -> T:
    """Return the first item, or default if there are none (like LINQ FirstOrDefault)."""
    return next(iter(items), default)


def group_by[T, K](items: Iterable[T], key: Callable[[T], K]) -> dict[K, list[T]]:
    """Group items into lists keyed by key(item) (like LINQ GroupBy)."""
    groups: dict[K, list[T]] = {}
    for item in items:
        groups.setdefault(key(item), []).append(item)
    return groups


def main() -> None:
    print(first_or_default([5, 6, 7], 0))
    print(first_or_default([], 0))
    print(group_by(["ana", "beto", "alan"], lambda s: s[0]))
    print(group_by([1, 2, 3, 4, 5], lambda n: n % 2 == 0))


if __name__ == "__main__":
    main()
