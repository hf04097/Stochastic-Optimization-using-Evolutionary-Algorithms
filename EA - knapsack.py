class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

class KnapsackEAInstance:
    def __init__(self, items):
        self.items = items
        self.value = -1
    
    def getFitness(self):
        if(self.value == -1):
            self.value = sum(self.items, key = lambda x: x.value)
        return self.value

class KnapsackEA:
    def __init__(self):
        self.allItems = []
        self.capacity = capacity
        
    def initializePopulation(self, popSize):
        