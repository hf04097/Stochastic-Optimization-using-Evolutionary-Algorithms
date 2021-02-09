import numpy as np
import random
import math
import matplotlib.pyplot as plt


class EA:
    def __init__(self, problem, parentSelection, survivorSelection):
        self.problem = problem
        self.parentSelection = parentSelection
        self.survivorSelection = survivorSelection

    def fitness(self, individual):
        return self.problem.fitness(individual)
        
    def crosover(self, individual1, individual2):
        return newIndividual = self.problem.crosover(individual1, individual2)

    def mutation(self, individual):
        if random.random() < self.mutRate:
            individual = self.problem.mutation(individual)
        return individual
        
    def genFitness(self);
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
            for offS in range(numOffSpring):
                parents = self.parentSelection(2)
                newIndividual = self.crosover(parents[0], parents[2])
                newIndividual = self.mutation(newIndividual)
                self.generation.append(newIndividual)
            
            self.generation = self.survivorSelection(numGen)
            genWiseFitness.append(self.genWiseFitness())
        
        genWiseFitness = np.array(genWiseFitness)
        
        
    
    def runKTimes(popSize, numGen, mutRate, numOffSpring, iterations):
        iterWiseFitness = []
        for i in range(iterations):
            iterWiseFitness.append(self.runOnce(popSize, numGen, mutRate, numOffSpring)
        iterWiseFitness = np.array(genWiseFitness)
        iterWiseAvgs = iterWiseFitness.mean(axis = 0)
        plt.plot(
            


EA(tsp(filename), f.binaryTrounamaent)