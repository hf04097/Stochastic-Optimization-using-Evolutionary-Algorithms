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

    class Selection:
        def __init__(self, population, selection_size,problem):
            self.selected = []
            self.population = population
            self.selection_size = selection_size
            self.problem = problem

        def FitnessProportionalSelection(self):
            sum_fitness = sum([self.problem.Fitness(route) for route in self.population])
            selection_prob = [self.problem.Fitness(route) / sum_fitness for route in self.population]
            for i in range(self.selection_size):
                self.selected.append(self.population[np.random.choice(len(self.population), p=selection_prob)])
            return self.selected

        def RankBasedSelection(self):
            worst_sorted_fitness = sorted(self.population, key=lambda agent: self.problem.Fitness(agent),reverse=True)
            ranks = np.arange(len(worst_sorted_fitness))
            selection_prob = [r / sum(ranks) for r in ranks]
            for i in range(self.selection_size):
                self.selected.append( worst_sorted_fitness[np.random.choice(len(worst_sorted_fitness), p=selection_prob)])
            return self.selected

        def BinaryTournamentSelection(self):
            for i in range(self.selection_size):
                binary = random.choices(self.population, k=2)
                sorted_binary = sorted(binary, key=lambda agent: self.problem.Fitness(agent), reverse=True)
                self.selected.append(sorted_binary[0])
            return self.selected

        def TruncationSelection(self):
            truncation_threshold = 0.5
            trunc = sorted(self.population, key=lambda agent: self.problem.Fitness(agent), reverse=True)[
                    :int(len(self.population) * truncation_threshold)]
            for i in range(self.selection_size):
                self.selected.append(trunc[random.randint(0, len(trunc) - 1)])

        def RandomSelection(self):
            return random.sample(self.population, self.selection_size)

    def Crossover(self, p1, p2):
        """
        :param p1: list containing genetic material for parent one
        :param p2: list containing genetic material for parent two
        :return: off spring produced through ordered crossover i.e
        """
        offspring_p1 = []

        gene_1 = int(random.random() * len(p1))
        gene_2 = int(random.random() * len(p1))

        start = min(gene_1, gene_2)
        end = max(gene_1, gene_2)

        for gene in range(start, end):
            offspring_p1.append(p1[gene])

        offspring_p2 = [gene for gene in p2 if gene not in offspring_p1]

        print(offspring_p1, offspring_p2, 'c')
        return offspring_p1 + offspring_p2

    def Mutation(self, individual):
        gene1 = random.randint(0, len(individual))
        gene2 = random.randint(0, len(individual))
        individual[gene1], individual[gene2] = individual[gene2], individual[gene1]
        return individual
