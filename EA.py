import numpy as np
import random
import math
import matplotlib.pyplot as plt
from tsp import TSP
from selection import Selection


class EA:
    def __init__(self, problem, parentSelection, survivorSelection):
        self.problem = problem
        self.parentSelection = parentSelection
        self.survivorSelection = survivorSelection

    def fitness(self, individual):
        return self.problem.Fitness(individual)
        
    def crosover(self, individual1, individual2):
        newIndividual = self.problem.Crossover(individual1, individual2)
        return newIndividual

    def mutation(self, individual):
        if random.random() < self.mutRate:
            individual = self.problem.Mutation(individual)
        return individual
        
    def genFitness(self):
        return [self.fitness(i) for i in self.generation]
        

    def runOnce(self, popSize, numGen, mutRate, numOffSpring):
        self.popSize = popSize
        self.numGen = numGen
        self.mutRate = mutRate
        self.numOffSpring = numOffSpring
        
        genWiseFitness = []
        self.generation = self.problem.initializePopulation(popSize)
        genWiseFitness.append(self.genFitness())
        
        for gen in range(numGen):
            parents = self.parentSelection(self.generation, numOffSpring * 2)
            # print(len(parents))
            for i in range(0, numOffSpring * 2, 2):
                newIndividual = self.crosover(parents[i], parents[i+1])
                newIndividual = self.mutation(newIndividual)
                self.generation.append(newIndividual)
            # print(len(self.generation), "yahan", popSize)
            self.generation = self.survivorSelection(self.generation, popSize)
            # print(len(self.generation), popSize, " ye wala")
            genWiseFitness.append(self.genFitness())
        
        genWiseFitness = np.array(genWiseFitness)
        genWiseFitnessAvgs = genWiseFitness.mean(axis = 1)
        genWiseFitnessMaxs = np.maximum.accumulate(genWiseFitness, axis = 1)
        return genWiseFitnessAvgs, genWiseFitnessMaxs
        
    
    def runKTimes(self, popSize = 30, numGen = 100, mutRate = 0.5, numOffSpring = 10, iterations = 10):
        iterWiseFitnessAvgs = []
        iterWiseFitnessMaxs = []
        for i in range(iterations):
            genWiseFitnessAvgs, genWiseFitnessMaxs = self.runOnce(popSize, numGen, mutRate, numOffSpring)
            iterWiseFitnessAvgs.append(genWiseFitnessAvgs)
            iterWiseFitnessMaxs.append(genWiseFitnessMaxs)
        iterWiseFitnessAvgs = np.array(iterWiseFitnessAvgs)
        iterWiseFitnessMaxs = np.array(iterWiseFitnessMaxs)
        iterWiseAvgs = iterWiseFitnessAvgs.mean(axis = 0)
        iterWiseMaxs = np.maximum.accumulate(iterWiseFitnessMaxs, axis = 0)
        plt.plot(range(len(iterWiseAvgs)), 1 / iterWiseAvgs)
        plt.xlabel("generations")
        plt.ylabel("average across iterations")
        plt.show()
        

population = 30
numGen = 500
mutRate = 0.5
numOffSpring = 10
iterations = 10
problem = TSP("city.tsp")
selobj = Selection(problem)

eaobject = EA(problem, selobj.BinaryTournamentSelection, selobj.FitnessProportionalSelection)
eaobject.runKTimes(population, numGen, mutRate, numOffSpring, iterations)





