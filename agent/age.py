import params


class Age:
    age: int

    def __init__(self, starting_age=0) -> None:
        self.age = starting_age

    @staticmethod
    def new():
        age = Age(0)
        return age

    @property
    def reproducible(self):
        return (self.age >= params.MIN_REPRODUCTION_AGE) and (
            self.age <= params.MAX_REPRODUCTION_AGE
        )

    def older(self, amount=1):
        self.age += amount

    def __repr__(self) -> str:
        return str(self.age)