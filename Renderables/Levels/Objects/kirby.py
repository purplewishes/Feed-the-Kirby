from Renderables.Levels.object import Object

class Kirby(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def step(self):
        pass

    def drawItems(self):
        return [['image', '../Images/Kirby.png', self.x, self.y]]