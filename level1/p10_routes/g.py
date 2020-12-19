from dataclasses import dataclass


@dataclass
class User:
    name: str
    age: int


u = User('tester', '15')
print(u)