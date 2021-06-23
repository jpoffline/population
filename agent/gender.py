import random

from params import MALE_FRAC


class Genders:
    MALE = "MALE"
    FEMALE = "FEMALE"


class Gender:
    reproducible: bool
    gender: str

    def __str__(self) -> str:
        return self.gender

    def __repr__(self) -> str:
        return self.__str__()

    @staticmethod
    def new():
        rand = random.random()
        if rand < MALE_FRAC:
            return Male()
        return Female()


class Male(Gender):

    gender = Genders.MALE
    reproducible = False


class Female(Gender):

    gender = Genders.FEMALE
    reproducible = True
