class Game:
    def __init__(self):
        self._rolls = []

    def roll(self, pins: int) -> None:
        self._rolls.append(pins)

    def score(self) -> int:
        total = 0
        i = 0
        for _ in range(10):
            if self._rolls[i] == 10:  # strike
                total += 10 + self._rolls[i + 1] + self._rolls[i + 2]
                i += 1
            elif self._rolls[i] + self._rolls[i + 1] == 10:  # spare
                total += 10 + self._rolls[i + 2]
                i += 2
            else:
                total += self._rolls[i] + self._rolls[i + 1]
                i += 2
        return total
