from PIL import Image, ImageDraw, ImagePath
import random
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
import os


class EvolutionArt:
    def __init__(self, actual_image, max_coordinate):
        self.number_coordinate = random.randrange(2, max_coordinate)
        self.coordinate = []
        self.actual_image = actual_image.convert('RGBA')

    def random_coordinate(self):
        # for i in range(self.number_coordinate):
        #     self.coordinate.append(
        #         (random.uniform(0, self.actual_image.size[0]), random.uniform(0, self.actual_image.size[1])))
        #     return self.coordinate
        return (random.uniform(0, self.actual_image.size[0]), random.uniform(0, self.actual_image.size[1]))

    def random_color(self):
        return tuple([random.randint(0, 255) for i in range(4)])

    def random_polygon(self):
        polygon_sides = 3
        vertices_list = []
        for i in range(polygon_sides):
            vertices_list.append(self.random_coordinate())
        return [vertices_list, self.random_color()]  # polygon individual with color

    def fitness(self, individual):
        diff_pixel = []
        for i in range(self.actual_image.size[0]):
            for j in range(self.actual_image.size[1]):
                r_act, g_act, b_act = self.actual_image.getpixel((i, j))
                r, g, b = individual.getpixel((i, j))
                diff_pixel.append((abs(r_act - r) + abs(g_act - g) + abs(b_act, b)) / 3)
        return sum(diff_pixel / len(diff_pixel))


# img = Image.open("mona_image.jpg")
# print(img.getpixel((2, 3)))
# gene = EvolutionArt(img, 4)
# print(gene.random_polygon())
#
# # img = Image.open("mona_image.jpg")
# # chromosome_img = Image.new(img.mode, img.size)
# # print(chromosome_img[0][0])
