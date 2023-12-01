from Renderables.Levels.object import Object

class Star(Object):

    def __init__(self, x, y):
        super().__init__(x, y, [], 5, 0.001)

    def drawItems(self): #returns image of star and location + rotation
        return [['image', '../Images/Star.png', self.x - 50, self.y - 50, 100, 100]]
