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
            self.value = sum([i * self.knapsack.allItems[i].value for i in self.items])
        return self.value
        
    def getWeight(self):
        return sum([self.knapsack.allItems[i].weight for i in self.items if i == 1])
        

class KnapsackEA:
    def __init__(self, fileName):
        file = open(fileName)
        items, capacity = map(int, file.readline().strip().split())
        self.allItems = []
        self.capacity = capacity
        for i in range(items):
            profit, weight = map(int, file.readline().strip().split())
            self.allItems.append(Item(weight, profit))
        
    def initializePopulation(self, popSize):
        gen = []
        while len(gen) < popSize:
            randomInit = KnapsackEAInstance([random.random() > 0.5 for i in range(len(self.allItems))], self)
            if randomInit.getWeight() <= self.capacity:
                gen.append(randomInit)
        return gen
    
    def Fitness(self, individual):
        return individual.getFitness()
    
    def Crossover(self, individual1, individual2):
        if random.random() > 0.5:
            individual1, individual2 = individual2, individual1
        cutoff = floor(random.random() * (len(self.allItems) - 1))
        newIndividual = KnapsackEAInstance(individual1.items[:cutoff + 1] + individual2.items[cutoff + 1:], self)
        while newIndividual.getWeight() > self.capacity:
            if random.random() > 0.5:
                individual1, individual2 = individual2, individual1
            cutoff = floor(random.random() * (len(allItems) - 1))
            newIndividual = KnapsackEAInstance(individual1.items[:cutoff + 1] + individual2.items[cutoff + 1:], self)
        return newIndividual
        
    def Mutation(self, individual):
        items = individual.items
        index = floor(random.random() * len(items))
        items[index] = not items[index]
        newIndividual = KnapsackEAInstance(items, self)
        while newIndividual.getWeight() > self.capacity:
            items[index] = not items[index]
            index = floor(random.random() * len(items))
            items[index] = not items[index]
            newIndividual = KnapsackEAInstance(items, self)
        return newIndividual
        
    
    
    
    