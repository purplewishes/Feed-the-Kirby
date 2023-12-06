from Renderables.Levels.object import Object

class Anchor(Object):
    def __init__(self, x, y):
        super().__init__(x, y, [], 14, 0)
        self.x = x
        self.y = y
    
    def calculateStep(self):
        pass

    def step(self):
        pass

    def drawItems(self):
        return [['circle', self.x, self.y, 10, 'brown', 100]]