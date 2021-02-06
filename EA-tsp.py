import numpy as np
import random
import math
import matplotlib.pyplot as plt
import os
import re

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

def read_tsp(tsp_name):
    with open(tsp_name) as f:
        for content in f:
            if content[0].isdigit():
                cords = content[content.index(" ") + 1:].split()
                citiesCord.append((float(cords[0]), float(cords[1])))
        return citiesCord

class City:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, x, y):
        x_diff = self.x - x
        y_diff = self.y - y
        return np.sqrt(x_diff ** 2 + y_diff ** 2)


citiesCord = []






