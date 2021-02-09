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
            parents = self.parentSelection(generation, numOffSpring * 2)
            for i in range(0, numOffSpring, 2):                
                newIndividual = self.crosover(parents[i], parents[i+1])
                newIndividual = self.mutation(newIndividual)
                self.generation.append(newIndividual)
            
            self.generation = self.survivorSelection(generation, numGen)
            genWiseFitness.append(self.genWiseFitness())
        
        genWiseFitness = np.array(genWiseFitness)
        genWiseFitnessAvgs = genWiseFitness.mean(axis = 1)
        genWiseFitnessMaxs = np.maximum.accumulate(genWiseFitness, axis = 1)
        return genWiseFitnessAvgs, genWiseFitnessMaxs
        
    
    def runKTimes(popSize, numGen, mutRate, numOffSpring, iterations):
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
        plt.plot(range(len(iterWiseAvgs)), iterWiseAvgs)
            


EA(tsp(filename), f.binaryTrounamaent)