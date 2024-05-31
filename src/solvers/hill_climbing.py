from .files import parse_input, dump_rides
from .objects.Rides import Rides
from .objects.CarGeneticRides import CarGeneticRides

# trial run
# a     time 000.0014s	score 4
# b     time 000.8203s	score 167,601
# c     time 534.0957s	score 6,673,587
# d     time 581.7603s	score 4,216,626
# e     time 560.0255s	score 15,667,106
# Global score is 26,724,924
# Total runtime is 1676.7033s


def hill_climbing(filename):

    rides, rows, cols, n_vehicles, bonus, t = parse_input("../assets/input/" + filename + ".in")
    CarGeneticRides.BONUS = bonus

    Rides.N_RIDES = len(rides) 
    Rides.N_CARS = n_vehicles

    solution = Rides(rides)
    solution.calculate_fitness()
    previous_score = 0

    while previous_score < solution.fitness:
        previous_score = solution.fitness
        solution = solution.hill_climbing_random()

    dump_rides("../assets/output/" + filename + ".out", solution.cars)
    return solution.fitness
