from PIL import Image, ImageDraw, ImagePath
import random
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
import os


class Gene():
    def __init__(self, actual_image, max_coordinate):
        self.number_coordinate = random.randrange(2, max_coordinate)
        self.coordinate = []
        self.actual_image = actual_image.convert('RGBA')

    def random_coordinate(self):
        for i in range(self.number_coordinate):
            self.coordinate.append(
                (random.uniform(0, self.actual_image.size[0]), random.uniform(0, self.actual_image.size[1])))
            return self.coordinate

    def random_color(self):
        return tuple([random.randint(0, 255) for i in range(4)])


img = Image.open("mona_image.jpg")
gene = Gene(img, 4)
print(gene.random_coordinate())
