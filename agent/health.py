import random


class Health:
    health: float

    def __init__(self, health) -> None:
        self.health = health

    @staticmethod
    def new(val=None):
        if val is not None:
            return Health(val)
        rand = random.random()
        if rand < 0.5:
            return Health(1.0)
        return Health(rand)

    def make_ill(self, amount):
        self.health -= amount
        if self.health < 0:
            return False
        return True

    def make_better(self, amount):
        self.health += amount
        if self.health < 0:
            return False
        return True

    def __repr__(self) -> str:
        return str(round(self.health, 2))
