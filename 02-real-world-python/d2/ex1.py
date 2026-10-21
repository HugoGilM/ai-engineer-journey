from __future__ import annotations

from pydantic import BaseModel, Field, ValidationError, model_validator


class Signup(BaseModel):
    username: str = Field(min_length=3, max_length=20, pattern=r"^[A-Za-z0-9_]+$")
    age: int = Field(ge=18)
    password: str = Field(min_length=8)
    confirm_password: str = Field(min_length=8)

    @model_validator(mode="after")
    def passwords_match(self) -> Signup:
        """Check that password and confirm_password are equal."""
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self


def main() -> None:
    """Demo a valid and an invalid signup."""
    ok = Signup(
        username="valid_user",
        age=30,
        password="securepassword",
        confirm_password="securepassword",
    )
    print(ok)

    try:
        bad = Signup(
            username="invalid user!",
            age=17,
            password="short",
            confirm_password="different",
        )
        print(bad)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
