from random import randint


class Weather:
    __chance_of_rain = 30

    def __init__(self):
        self.randomize()
        self._is_raining = False

    @property
    def is_raining(self):
        return self._is_raining

    @is_raining.setter
    def is_raining(self, state: bool):
        self._is_raining = state

    def randomize(self):
        self._is_raining = randint(0, 101) < self.__chance_of_rain


if __name__ == "__main__":
    pass
