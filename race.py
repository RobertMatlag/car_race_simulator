from weather import Weather
from vehicles import Truck


class Race:
    __num_of_laps = 50

    def __init__(self):
        self.__broken_truck = False
        self.__vehicles = list()
        self.__weather = Weather()

    def simulate_race(self):
        for i in range(self.__num_of_laps):
            for vehicle in self.__vehicles:
                vehicle.prepare_for_lap(self)
                vehicle.move_for_hour()

            self.__weather.randomize()
            self.__broken_truck = self.__get_broken_car_status()

    def __get_broken_car_status(self):
        for vehicle in self.__vehicles:
            if isinstance(vehicle, Truck):
                if vehicle.is_broken_down():
                    return True

        return False

    def register_racer(self, racer):
        self.__vehicles.append(racer)

    def is_raining(self):
        return self.__weather.is_raining

    def is_yellow_flag_active(self):
        return self.__broken_truck

    def print_race_results(self):
        print("Race results")
        for vehicle in self.__vehicles:
            print(vehicle)


if __name__ == "__main__":
    pass
