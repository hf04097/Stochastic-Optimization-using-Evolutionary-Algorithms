import numpy as np
import random
import math
import matplotlib.pyplot as plt


class EA:
    def __init__(problem, parentSelection, survivorSelection):
        self.problem = problem

    def fitness(individual):
        self.problem.fitness(individual)
        
    def crosover(individual1, individual2):
        self.problem.crosover(individual1, individual2)

    def mutation(individual):
        if random.random() < self.mutationRate:
            self.problem.mutation(individual)

    def runOnce(popSize, numGen, mutRate, numOffSpring):
        self.popSize = popSize
        self.numGen = numGen
        self.mutRate = mutRate
        self.numOffSpring = numOffSpring
        
        self.problem.
    
    def runKTimes(popSize, numGen, mutRate, numOffSpring, iterations):
        pass


EA(problem, f.binaryTrounamaent())