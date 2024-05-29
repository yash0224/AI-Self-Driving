import os
import random
from .files import parse_input, dump_rides
from .objects.Rides import Rides
from .objects.CarGeneticRides import CarGeneticRides

# trial run
# a     time 000.0012s 	score 4
# b     time 000.0438s 	score 161,266
# c     time 001.6680s 	score 6,744,998
# d     time 001.7412s 	score 4,138,429
# e     time 001.9867s 	score 15,619,361
# Global score is 26,664,058
# Total runtime is 5.4411s


def simulated_annealing(filename):
    rides, rows, cols, n_vehicles, bonus, t = parse_input("../assets/input/" + filename + ".in")

    CarGeneticRides.BONUS = bonus
    Rides.N_RIDES = len(rides)
    Rides.N_CARS = n_vehicles

    solution = Rides(rides)
    solution.calculate_fitness()
    previous_score = 0
    temperature = len(rides)

    while temperature > 0.1 or previous_score != solution.fitness:
        previous_score = solution.fitness
        solution.simulated_annealing(temperature)
        temperature = random.uniform(0.8, 0.99) * temperature

    dump_rides("../assets/output/" + filename + ".out", solution.cars)
    return solution.fitness
