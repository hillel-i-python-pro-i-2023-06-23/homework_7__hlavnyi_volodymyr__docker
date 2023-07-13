from typing import NamedTuple
from collections.abc import Iterator

from app.services.faker_instance import faker


class User(NamedTuple):
    username: str
    email: str

    def get_dict(self) -> dict:
        return self._asdict()

    @classmethod
    def get_fieldnames(cls) -> list[str]:
        return list(cls._fields)

    @classmethod
    def from_raw_dict(cls, raw_data: dict) -> "User":
        return cls(
            username=raw_data["username"],
            email=raw_data["email"],
        )


def generate_user() -> User:
    return User(
        username=faker.first_name(),
        email=faker.email(),
    )


def generate_users(amount: int = 100) -> Iterator[User]:
    for index in range(1, amount + 1):
        yield generate_user()


def print_users(users, is_print_index=False):
    for index4print, user in enumerate(users):
        string4print = f"Name: {user.username}, email:{user.email}"
        if is_print_index:
            string4print = f"{index4print} Name: {user.username}, email:{user.email}"
        print(string4print)
