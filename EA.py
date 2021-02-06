import numpy as np
import random
import math
import matplotlib.pyplot as plt



class Fitness:
    def __init__(self, route):
        self.route = route
        self.fitness = 0.0
        self.distance = 0.0


