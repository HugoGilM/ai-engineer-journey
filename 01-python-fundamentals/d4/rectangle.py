class Rectangle:
    """A rectangle with validated, positive dimensions."""

    def __init__(self, width: float, height: float) -> None:
        self.width = width  # Goes through the setter, so it's validated too.
        self.height = height

    @property
    def width(self) -> float:
        return self._width

    @width.setter
    def width(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"width must be positive, got {value}")
        self._width = value

    @property
    def height(self) -> float:
        return self._height

    @height.setter
    def height(self, value: float) -> None:
        if value <= 0:
            raise ValueError(f"height must be positive, got {value}")
        self._height = value

    @property
    def area(self) -> float:
        """Read-only: there is no setter, so assigning to it raises AttributeError."""
        return self.width * self.height

    @classmethod
    def square(cls, size: float) -> "Rectangle":
        """Alternative constructor for a rectangle with equal sides."""
        return cls(size, size)

    def __repr__(self) -> str:
        return f"Rectangle(width={self.width}, height={self.height})"


if __name__ == "__main__":
    r = Rectangle(3, 4)
    print(r, "area:", r.area)

    sq = Rectangle.square(5)
    print(sq, "area:", sq.area)

    r.width = 10
    print("after resize:", r, "area:", r.area)

    try:
        r.width = -2
    except ValueError as e:
        print("ValueError:", e)

    try:
        r.area = 100
    except AttributeError as e:
        print("AttributeError:", e)
