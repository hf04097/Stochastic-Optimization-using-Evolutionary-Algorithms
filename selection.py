import random
import numpy as np


class Selection:
    def __init__(self, population, selection_size):
        self.selected = []
        self.population = population
        self.selection_size = selection_size

    def FitnessProportionalSelection(self):
        for i in range(self.selection_size):
            sum_fitness = sum([Fitness(route).routeFitness() for route in self.population])
            selection_prob = [Fitness(route).routeFitness() / sum_fitness for route in self.population]
            self.selected.append(self.population[np.random.choice(len(self.population), p=selection_prob)])
        return self.selected

    def RankBasedSelection(self):
        return 0

    def BinaryTournamentSelection(self):
        for i in range(self.selection_size):
            binary = random.choices(self.population, k=2)
            sorted_binary = sorted(binary, key=lambda agent: Fitness(agent).routeFitness(), reverse=True)
            self.selected.append(sorted_binary[0])
        return self.selected

    def TruncationSelection(self):
        truncation_threshold = 0.5
        trunc = sorted(self.population, key=lambda agent: Fitness(agent).routeFitness(), reverse=True)[
                :int(len(self.population) * truncation_threshold)]
        for i in range(self.selection_size):
            self.selected.append(trunc[random.randint(0, len(trunc) - 1)])

    def RandomSelection(self):
        return random.sample(self.population, self.selection_size)
