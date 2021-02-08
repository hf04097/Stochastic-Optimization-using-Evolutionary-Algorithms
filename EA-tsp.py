import numpy as np
import random
import math
import matplotlib.pyplot as plt
import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, city):
        x_diff = city.x - self.x
        y_diff = city.y - self.y
        return np.sqrt(x_diff ** 2 + y_diff ** 2)


def create_cities_list(tsp_name):
    """
    :param tsp_name: filename which contains co ordinates of the city. Format of the file is like this:
    ['NAME: ulysses16.tsp',
    'TYPE: TSP',
    'COMMENT: Odyssey of Ulysses (Groetschel/Padberg)',
    'DIMENSION: 16',
    'EDGE_WEIGHT_TYPE: GEO',
    'DISPLAY_DATA_TYPE: COORD_DISPLAY',
    'NODE_COORD_SECTION',
    '1 38.24 20.42',
    '2 39.57 26.15',
    '3 40.56 25.32',
    ................
    'EOF']
    :return: A list of City objects where x and y are city co ordinates.
    """
    cities_cord = []
    with open(tsp_name) as f:
        for content in f:
            if content[0].isdigit():
                cords = content[content.index(" ") + 1:].split()
                # cities_cord.append((float(cords[0]), float(cords[1])))
                cities_cord.append(City(x=float(cords[0]), y=float(cords[1])))
        return cities_cord


class Fitness:
    def __init__(self, route):
        self.route = route
        self.fitness = 0.0
        self.distance = 0.0

    def routeDistance(self):
        route_len = len(self.route)
        path_distance = 0
        for i in range(1, route_len):
            start_city = self.route[i - 1]
            end_city = self.route[i]
            path_distance += start_city.distance(end_city)  # calculating distance between two cities in the route
        self.distance = path_distance
        return self.distance

    def routeFitness(self):
        if self.fitness == 0:
            self.fitness = 1 / float(self.routeDistance())  # inverse as we are minimizing it
        return self.fitness


def initializePopulation(pop_size, cities_list):
    population = []
    for i in range(pop_size):
        route_possible = random.sample(cities_list, len(
            cities_list))  # getting a route from all cities (as all cities have a path to each other)
        population.append(route_possible)
    return population


class Selection:
    def __init__(self, population):
        self.selected_parents = []
        self.population = population

    def FitnessProportionalSelection(self):
        sum_fitness = sum([Fitness(route).routeFitness() for route in self.population])
        selection_prob = [Fitness(route).routeFitness() / sum_fitness for route in self.population]
        return self.population[np.random.choice(len(self.population), p=selection_prob)]

    def RankBasedSelection(self):
        return 0

    def BinaryTournamentSelection(self):
        binary = random.choices(self.population, k=2)
        sorted_binary = sorted(binary, key=lambda agent: Fitness(agent).routeFitness(), reverse=True)
        return sorted_binary[0]

    def TruncationSelection(self):
        return sorted(self.population, key=lambda agent: Fitness(agent).routeFitness(), reverse=True)[0]

    def RandomSelection(self):
        return random.choice(self.population)


def breed(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random.random() * len(parent1))
    geneB = int(random.random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    print(childP1, childP2, 'c')
    child = childP1 + childP2
    return child


#print(breed([1, 2, 3, 4, 5], [6, 7, 8, 9, 10]))

cities_x_y = create_cities_list('city.tsp')
population = initializePopulation(30, cities_x_y)

# for i in population:
#     print(Fitness(i).routeFitness())


print(Selection(population).FitnessProportionalSelection())
# print(Selection(population).BinaryTournamentSelection())
# print(Selection(population).TruncationSelection())
