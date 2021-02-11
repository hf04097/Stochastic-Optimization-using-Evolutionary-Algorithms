import numpy as np
import random


class Selection:
    def __init__(self, problem):
        self.selected = []
        # self.population = population
        # self.selection_size = selection_size
        self.problem = problem

    def FitnessProportionalSelection(self, population, selection_size):
        sum_fitness = sum([self.problem.Fitness(route) for route in population])
        selection_prob = [self.problem.Fitness(route) / sum_fitness for route in population]
        self.selected = []
        for i in range(selection_size):
            # print(np.random.choice(len(population), 1, p = selection_prob))
            self.selected.append(population[np.random.choice(len(population), 1, p=selection_prob).tolist()[0]])
        return self.selected

    def RankBasedSelection(self, population, selection_size):
        self.selected = []
        worst_sorted_fitness = sorted(population, key=lambda agent: self.problem.Fitness(agent))
        ranks = np.arange(1, len(worst_sorted_fitness) + 1, 1)
        selection_prob = [r / sum(ranks) for r in ranks]
        for i in range(selection_size):
            self.selected.append(worst_sorted_fitness[np.random.choice(len(worst_sorted_fitness), p=selection_prob)])
        return self.selected

    def BinaryTournamentSelection(self, population, selection_size):
        self.selected = []
        for i in range(selection_size):
            binary = random.choices(population, k=2)
            sorted_binary = sorted(binary, key=lambda agent: self.problem.Fitness(agent), reverse=True)
            self.selected.append(sorted_binary[0])
        return self.selected

    def TruncationSelection(self, population, selection_size):
        self.selected = []
        truncation_threshold = 0.5
        trunc = sorted(population, key=lambda agent: self.problem.Fitness(agent), reverse=True)[
                :max(int(len(population) * truncation_threshold), 1)]
        for i in range(selection_size):
            self.selected.append(trunc[random.randint(0, len(trunc) - 1)])
        return self.selected

    def RandomSelection(self, population, selection_size):
        return random.choices(population, k = selection_size)
