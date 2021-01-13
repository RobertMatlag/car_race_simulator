from abc import ABC, abstractmethod
from random import randint, choices


class Vehicle(ABC):
    def __init__(self, normal_speed: int):
        self._name = self.generate_name()
        self._normal_speed = normal_speed
        self._actual_speed = 0
        self._distance_travelled = 0

    @abstractmethod
    def prepare_for_lap(self, race):
        pass

    @abstractmethod
    def generate_name(self):
        pass

    def move_for_hour(self):
        self._distance_travelled += self._actual_speed

    def __str__(self):
        return f"{{distance travelled: {self._distance_travelled}, type: {type(self).__name__}, name: {self._name}}}"


class Car(Vehicle):
    __possible_names = "Epiphany", "Parallel", "Blitz", "Eos", "Evolution", "Wolf", "Union", "Empyrean", "Curiosity", "Gallop"
    __yellow_flag_speed = 75

    def __init__(self):
        super().__init__(self.__calculate_normal_speed())

    def prepare_for_lap(self, race):
        self._actual_speed = self.__yellow_flag_speed if race.is_yellow_flag_active() else self._normal_speed

    def generate_name(self):
        return " ".join(choices(self.__possible_names, k=2))

    @staticmethod
    def __calculate_normal_speed():
        return randint(80, 110 + 1)


class Truck(Vehicle):
    __normal_speed = 100
    __breakdown_chance = 5
    __turns_needed_to_fix_truck = 2

    def __init__(self):
        super().__init__(self.__normal_speed)
        self.__breakdown_turns_left = 0
        self.__ready = True

    def prepare_for_lap(self, race):
        self._actual_speed = 0 if self.is_broken_down() else self._normal_speed
        self.__ready = self.__next_state()

    def generate_name(self):
        return str(randint(1, 1001))

    def is_broken_down(self):
        return not self.__ready

    def __next_state(self):
        if self.__ready:
            if randint(0, 101) < self.__breakdown_chance:
                self.__breakdown_turns_left = self.__turns_needed_to_fix_truck
                return False
        else:
            self.__breakdown_turns_left -= 1
            if self.__breakdown_turns_left > 0:
                return False

        return True


class Motorcycle(Vehicle):
    __normal_speed = 100
    __motorcycle_number = 1

    def __init__(self):
        super().__init__(self.__normal_speed)

    def prepare_for_lap(self, race):
        self._actual_speed = self._normal_speed

        if race.is_raining():
            self._actual_speed -= randint(5, 50 + 1)

    def generate_name(self):
        name = f"Motorcycle {__class__.__motorcycle_number}"
        __class__.__motorcycle_number += 1
        return name


if __name__ == "__main__":
    pass
