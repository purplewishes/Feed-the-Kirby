from Renderables.Levels.object import Object

class Bubble(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def step(self):
        pass
    
    def calculateStep(self):
        pass

    def drawItems(self):
        return [['image', '../Images/Bubble.png', self.x, self.y, 100, 100]]