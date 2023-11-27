from Renderables.Levels.object import Object

class Point(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def step(self): #updates object
        pass

    def drawItems(self): #returns list of drawables
        return [['image', '../Images/Point.png', self.x, self.y]]