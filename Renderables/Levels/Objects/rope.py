from Renderables.Levels.object import Object

class RopeSegment(Object):
    def __init__(self, x, y, leftNeighbor, rightNeighbor):
        self.x = x
        self.y = y
        self.leftNeighbor = leftNeighbor
        self.rightNeighbor = rightNeighbor
    
    def step(self):
        pass

    def drawItems(self):
        pass