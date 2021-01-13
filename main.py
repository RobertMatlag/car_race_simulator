from race import Race
from vehicles import Car, Motorcycle, Truck


def create_vehicles(race: Race):
    for i in range(10):
        race.register_racer(Car())
        race.register_racer(Motorcycle())
        race.register_racer(Truck())


if __name__ == '__main__':
    race_simulation = Race()
    create_vehicles(race_simulation)

    race_simulation.simulate_race()
    race_simulation.print_race_results()
