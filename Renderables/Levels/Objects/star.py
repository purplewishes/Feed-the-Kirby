from Renderables.Levels.object import Object

class Star(Object):

    def __init__(self, x, y, connectedObjects):
        self.x = x
        self.y = y 
        self.connectedObjects = connectedObjects

    def step(self):
        pass

    def drawItems(self): #returns image of star and location + rotation
        return [['image', '../Images/Star.png', self.x, self.y]]
