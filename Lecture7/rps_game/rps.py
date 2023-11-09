from enum import Enum

class Choice(Enum):
    ROCK = 0
    PAPER = 1
    SCISSORS = 2

    @classmethod
    def from_str(cls, s: str) -> "Choice":
        try:
            return {
                "r": cls.ROCK,
                "rock": cls.ROCK,
                "p": cls.PAPER,
                "paper": cls.PAPER,
                "s": cls.SCISSORS,
                "scissors": cls.SCISSORS
            }[s.strip().lower()]
        except KeyError:
            raise ValueError(f"{s!r} is not a valid {cls.__name__}")

    def __str__(self) -> str:
        return self.name.lower()

    def beats(self, other: "Choice") -> bool:
        return (self.value - other.value) % 3 == 1