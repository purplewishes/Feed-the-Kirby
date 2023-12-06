from Renderables.Levels.object import Object

class Point(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self): 
        pass

    def calculateStep(self):
        pass

    def drawItems(self): 
        return [['circle', self.x, self.y, 15, "cyan", 70]]