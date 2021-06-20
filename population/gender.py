import random


class Genders:
    MALE = "MALE"
    FEMALE = "FEMALE"


class Gender:
    reproducible = None
    gender = None

    @property
    def can_birth(self):
        return self.reproducible

    def __str__(self) -> str:
        return self.gender

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def new():
        rand = random.random()
        if rand < 0.5:
            return Male()
        return Female()


class Male(Gender):

    gender = Genders.MALE

    @property
    def can_birth(self):
        return False


class Female(Gender):

    gender = Genders.FEMALE

    @property
    def can_birth(self):
        return True
