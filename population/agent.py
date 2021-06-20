from dataclasses import dataclass
import random

from population.gender import Gender


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

    def __repr__(self) -> str:
        return str(round(self.health, 2))


class Agent:
    id: int
    age: float
    alive: bool
    gender: Gender
    just_reproduced: bool
    health: Health
    parent_id: int

    def __init__(
        self,
        id=id,
        age=None,
        alive=True,
        health=None,
        gender=None,
        just_reproduced=False,
        parent_id=None,
    ) -> None:

        self.id = id
        self.age = age
        self.alive = alive
        self.health = health
        self.gender = gender
        self.just_reproduced = just_reproduced
        self.parent_id = parent_id
        self.child_id = None

    @staticmethod
    def new(id, parent_id=None):
        new_age = 0
        health = Health.new()
        gender = Gender.new()
        just_reproduced = False
        return Agent(
            id=id,
            age=new_age,
            alive=True,
            health=health,
            gender=gender,
            just_reproduced=just_reproduced,
            parent_id=parent_id,
        )

    @property
    def can_reproduce(self):
        if not self.alive:
            return False
        if self.just_reproduced:
            self.just_reproduced = False
            return False
        if self.age == 0:
            return False
        if not self.gender.can_birth:
            return False
        return True

    @property
    def reproduce(self):
        if self.can_reproduce:
            self.just_reproduced = True
            return True
        return False

    def give_birth(self, id):
        child = Agent.new(id, parent_id=self.id)
        child.health = self.health
        self.child_id = id
        return child

    def make_older(self, amount=1):
        self.age += amount

        if not self.health.make_ill(0.1):
            self.kill()

    def kill(self):
        self.alive = False

    def __repr__(self) -> str:
        return f"id={self.id} Age={self.age} {self.can_reproduce} Health={self.health} Gender={self.gender} Parent={self.parent_id} Child={self.child_id}"