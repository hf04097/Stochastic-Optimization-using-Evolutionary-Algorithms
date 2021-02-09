import numpy as np
import random
import os
import operator

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


class TSP:
    def __init__(self, filename):
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
        """
        self.filename = filename

    class City:
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def distance(self, city):
            x_diff = city.x - self.x
            y_diff = city.y - self.y
            return np.sqrt(x_diff ** 2 + y_diff ** 2)

    def create_cities_list(self):
        """
        :return: A list of City objects where x and y are city co ordinates.
        """
        cities_cord = []
        with open(self.filename) as f:
            for content in f:
                if content[0].isdigit():
                    cords = content[content.index(" ") + 1:].split()
                    # cities_cord.append((float(cords[0]), float(cords[1])))
                    cities_cord.append(self.City(x=float(cords[0]), y=float(cords[1])))
            return cities_cord

    def initializePopulation(self, pop_size):
        cities_list = self.create_cities_list()
        """
        :param pop_size: the subset size of the current generation
        :param cities_list: a list of City objects with x and y co ordinates.
        :return: list which contains pop_size routes
        """
        population = []
        for i in range(pop_size):
            route_possible = random.sample(cities_list, len(
                cities_list))  # getting a route from all cities (as all cities have a path to each other)
            population.append(route_possible)
        return population

    def Fitness(self, route):
        fitness = 0.0
        """
        :return: a float which is the distance from the starting city to end city in the path taken to complete the route.
        """
        route_len = len(route)
        path_distance = 0
        for i in range(1, route_len):
            start_city = route[i - 1]
            end_city = route[i]
            path_distance += start_city.distance(end_city)  # calculating distance between two cities in the route
        distance = path_distance
        if fitness == 0.0:
            fitness = 1 / float(distance)
        return fitness

    def Crossover(self, p1, p2):
        """
        :param p1: list containing genetic material for parent one
        :param p2: list containing genetic material for parent two
        :return: off spring produced through ordered crossover i.e
        """
        offspring_p1 = []

        gene_1 = int(random.random() * len(p1))
        gene_2 = int(random.random() * len(p2))

        start = min(gene_1, gene_2)
        end = max(gene_1, gene_2)

        for gene in range(start, end):
            offspring_p1.append(p1[gene])

        offspring_p2 = [gene for gene in p2 if gene not in offspring_p1]

        # print(offspring_p1, offspring_p2, 'c')
        return offspring_p1 + offspring_p2

    def Mutation(self, individual):
        gene1 = random.randint(0, len(individual) - 1)
        gene2 = random.randint(0, len(individual) - 1)
        individual[gene1], individual[gene2] = individual[gene2], individual[gene1]
        return individual
