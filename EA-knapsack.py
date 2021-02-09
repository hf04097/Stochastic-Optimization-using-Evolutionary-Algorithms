import random
from math import floor


class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value


class KnapsackEAInstance:
    def __init__(self, items, knapsack):
        self.items = items
        self.value = -1
        self.knapsack = knapsack
    
    def getFitness(self):
        if(self.value == -1):
            self.value = sum([i * knapsack.allItems[i].value for i in items])
        return self.value
        
    def getWeight(self):
        return sum([knapsack.allItems[i].weight for i in items if i == 1])
        

class KnapsackEA:
    def __init__(self):
        self.allItems = []
        self.capacity = capacity
        
    def initializePopulation(self, popSize):
        gen = []
        while len(gen) < popSize:
            randomInit = KnapsackEAInstance([random.random() > 0.5 for i in range(len(self.allItems))], self)
            if randomInit.getWeight() <= capacity:
                gen.append(randomInit)
        return gen
    
    def fitness(self, individual):
        return individual.fitness()
    
    def crossover(self, individual1, individual2):
        if random.random() > 0.5:
            individual1, individual2 = individual2, individual1
        cutoff = floor(random.random() * (len(allItems) - 1))
        newIndividual = KnapsackEAInstance(individual1.items[:cutoff + 1] + individual2[cutoff + 1:])
        while newIndividual.getWeight > capacity:
            if random.random() > 0.5:
                individual1, individual2 = individual2, individual1
            cutoff = floor(random.random() * (len(allItems) - 1))
            newIndividual = KnapsackEAInstance(individual1.items[:cutoff + 1] + individual2[cutoff + 1:])
        return newIndividual
        
    def mutation(self, individual):
        items = individual.items
        index = floor(random.random() * len(items))
        items[index] = not items[index]
        newIndividual = KnapsackEAInstance(items, self)
        while newIndividual.getWeight() > capacity:
            items[index] = not items[index]
            index = floor(random.random() * len(items))
            items[index] = not items[index]
            newIndividual = KnapsackEAInstance(items, self)
        return newIndividual
        
    
    
    
    