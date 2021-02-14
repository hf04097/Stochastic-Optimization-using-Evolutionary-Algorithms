from PIL import Image, ImageDraw, ImagePath
import random
import numpy as np
from matplotlib import pyplot as plt
import math
import os
# import cv2


class Polygon:
    def __init__(self, img_size, polSideLower = 3, polSideUpper = 3):
        if polSideLower == polSideUpper:
            self.number_coordinates = polSideLower
        else:
            self.number_coordinates = random.randrange(polSideLower, polSideUpper)
        self.coordinates = []
        self.color = tuple()
        self.size = img_size
        self.random_polygon()
        # self.actual_image = actual_image.convert('RGBA')
        
    def random_coordinate(self):
        # for i in range(self.number_coordinate):
        #     self.coordinate.append(
        #         (random.uniform(0, self.actual_image.size[0]), random.uniform(0, self.actual_image.size[1])))
        #     return self.coordinate
        return (random.uniform(0, self.size[1]), random.uniform(0, self.size[0]))

    def random_color(self):
        self.color = tuple([random.randint(0, 255) for i in range(3)] + [random.randint(0, 255)])
        return self.color

    def random_polygon(self):
        polygon_sides = self.number_coordinates
        self.coordinates = []
        for i in range(polygon_sides):
            self.coordinates.append(self.random_coordinate())
        return [self.coordinates, self.random_color()]  # polygon individual with color
    
            


class ArtIndividual:
    def __init__(self, img_arr):
        self.sideCount = 6
        self.hexasize = 50
        self.img_arr = img_arr
        self.fitness = -1
    
    def randomInit(self, polCount = 5, polSideLower = 3, polSideUpper = 3):
        # return self.randomInit1(polCount, polSideLower, polSideUpper)
        return self.randomInit1(polCount)

    def randomInit1(self, polCount = 50, polSideLower = 3, polSideUpper = 3):
        self.polSideLower = polSideLower
        self.polSideUpper = polSideUpper
        self.polygons = [Polygon(self.img_arr.shape[0:2], polSideLower, polSideUpper).random_polygon() for i in range(polCount)]
        return self

    def randomRegularPolygon(self):
        thetaInc = math.radians(360 / self.sideCount)
        points = []
        origin = (random.uniform(0, self.img_arr.shape[1]), random.uniform(0, self.img_arr.shape[0]))
        for i in range(self.sideCount):
            offset = (self.hexasize * math.cos(thetaInc * i), self.hexasize * math.sin(thetaInc * i))
            point = (offset[0] + origin[0], offset[1] + origin[1])
            points.append(tuple(point))
        colour = tuple([random.randint(0, 255) for i in range(3)] + [70])
        return [points, colour]

    def randomInit2(self, polCount = 50):
        self.polygons = []
        for j in range(polCount):
            self.polygons.append(self.randomRegularPolygon())
        return self


    def setPolygons(self, polygons):
        self.polygons = polygons
        self.polSideLower = 3
        self.polSideUpper = 3
        return self

    def getFitness(self):
        if self.fitness == -1:
            img = Image.new("RGBA", self.img_arr.shape[0:2][::-1], "black")
            for pol in self.polygons:
                img2 = Image.new("RGBA", self.img_arr.shape[0:2][::-1], (255,255,255,0))
                img3 = ImageDraw.Draw(img2)
                img3.polygon(pol[0], fill = pol[1])
                img = Image.alpha_composite(img, img2)
            img = img.convert("RGB")
            self.constructed_img = np.array(img)
            self.fitness = ((self.img_arr - self.constructed_img) ** 2).sum()
        return 1 / self.fitness
    
    def mutate1(self):
        randInd = random.randint(0, len(self.polygons) - 1)
        if random.random() < 0.5:
            colInd = random.randint(0, 3)
            polCol = self.polygons[randInd][1]
            newPolCol = polCol[:colInd] + (random.randint(0, 255),) + polCol[colInd + 1:]
            self.polygons[randInd][1] = newPolCol
        else:
            coordInt = random.randint(0, len(self.polygons[randInd][0]) - 1)
            if random.random() < 0.5:
                newX = random.uniform(0, self.img_arr.shape[0])
                currentCoord = self.polygons[randInd][0][coordInt]
                self.polygons[randInd][0][coordInt] = (newX, currentCoord[1])
            else:
                newY = random.uniform(0, self.img_arr.shape[1])
                currentCoord = self.polygons[randInd][0][coordInt]
                self.polygons[randInd][0][coordInt] = (currentCoord[0], newY)

    def mutate2(self):
        randInd = random.randint(0, len(self.polygons) - 1)
        self.polygons[randInd] = Polygon(self.img_arr.shape[0:2], self.polSideLower, self.polSideUpper).random_polygon()
        # self.polygons[randInd] = self.randomRegularPolygon()

    def mutate(self):
        self.mutate2()

    def increasePolCount(self):
        if len(self.polygons) < 50:
            self.polygons.append(Polygon(self.img_arr.shape[0:2], self.polSideLower, self.polSideUpper).random_polygon())


class EvolutionaryArt:
    def __init__(self, filename):
        self.img_arr = np.array(Image.open(filename))

    def initializePopulation(self, popSize):
        gen = [ArtIndividual(self.img_arr).randomInit() for i in range(popSize)]
        return gen

    def Fitness(self, individual):
        return individual.getFitness()

    def Crossover(self, individual1, individual2):
        return self.Crossover2(individual1, individual2)

    def Crossover1(self, individual1, individual2):
        if len(individual1.polygons) > len(individual2.polygons):
            individual1, individual2 = individual2, individual1
        elif len(individual1.polygons) == len(individual2.polygons):
            if random.random() < 0.5:
                individual1, individual2 = individual2, individual1
        ind1 = int(random.random() * (len(individual1.polygons) - 1))
        count = int((len(individual1.polygons) - 1 - ind1) * random.random() + 1)
        return ArtIndividual(self.img_arr).setPolygons(individual1.polygons[:ind1 + 1] + individual2.polygons[ind1 + 1: ind1 + count + 1] + individual1.polygons[ind1 + count + 1:])

    def Crossover2(self, individual1, individual2):
        pol1 = individual1.polygons
        pol2 = individual2.polygons
        selection_prob = list(range(1, len(pol1) + 1))
        selection_prob = [i / sum(selection_prob) for i in selection_prob]
        ind1 = np.random.choice(len(pol1), p = selection_prob)
        return ArtIndividual(self.img_arr).setPolygons(pol1[:ind1] + pol2[ind1:])

    def Mutation(self, individual):
        individual.mutate()
        return individual

    def housework(self, genNum, population, fitnesses):
        best = max(fitnesses)
        ind = fitnesses.index(best)
        if (genNum + 1) % 10 == 0:
            plt.imshow(population[ind].constructed_img)
            print("Saved Gen Num" + str(genNum + 1))
            plt.savefig("Progress/" + str(genNum + 1) + ".jpg")
            plt.clf()
        
        if (genNum + 1) % 30 == 0:
            for i in population:
                i.increasePolCount()



# img = Image.open("mona_image.jpg")
# print(img.getpixel((2, 3)))
# gene = Polygon(img, 4)
# print(gene.random_polygon())
#
# # img = Image.open("mona_image.jpg")
# # chromosome_img = Image.new(img.mode, img.size)
# # print(chromosome_img[0][0])

# img = Image.new("RGBA", (100, 100), "black")
# img1 = ImageDraw.Draw(img)
# img1.polygon([(0,0), (0,50), (50,0)], (255,0,0,200))
# img1.polygon([(30,0), (30,50), (80,30)], (0,255,0,250))
# img.show()

