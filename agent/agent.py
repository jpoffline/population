from agent.health import Health
from agent.gender import Gender
from agent.location import Location
from agent.age import Age
import random
import params


class Agent:
    id: int
    age: Age
    alive: bool
    gender: Gender
    just_reproduced: bool
    health: Health
    parent_id: int
    location: Location

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
        self.child_ids = []

    @staticmethod
    def new(id, parent_id=None):
        new_age = Age.new()
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
        if not self.age.reproducible:
            return False
        if not self.gender.reproducible:
            return False
        if self.just_reproduced:
            self.just_reproduced = False
            return False
        if self.health.health < params.MIN_REPRODUCTION_HEALTH:
            return False
        return True

    @property
    def will_reproduce(self):
        if not self.can_reproduce:
            return False
        if random.random() < params.RAND_INFERTILE:
            return False
        self.just_reproduced = True
        return True

    def give_birth(self, id):
        child = Agent.new(id, parent_id=self.id)
        self.child_ids.append(id)
        return child

    def make_older(self, amount=1):
        self.age.older(amount=amount)
        self.update_health()

    def update_health(self):
        r = random.random()
        # if r < 0.4:
        # self.health.make_better(0.01)
        if not self.health.make_ill(0.1):
            self.kill()

    def kill(self):
        self.alive = False

    def __repr__(self) -> str:
        return (
            f"id={self.id} Age={self.age} {self.can_reproduce} "
            f"Health={self.health} Gender={self.gender} Parent={self.parent_id} Child={self.child_ids}"
        )
