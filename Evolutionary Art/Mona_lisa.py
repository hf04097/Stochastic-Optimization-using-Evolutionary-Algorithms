from PIL import Image, ImageDraw, ImagePath
import random
import numpy as np
from matplotlib import pyplot as plt
import cv2
import math
import os

class Gene():
    def __init__(self,max_vertices):
        self.number_vertices = random.randrange(2,max_vertices)

