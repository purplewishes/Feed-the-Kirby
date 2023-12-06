from Renderables.Levels.object import Object

class RopeSegment(Object):
    def __init__(self, x, y, leftNeighbor, rightNeighbor, d=3, k=6, m=0.08, air=0.0005):
        super().__init__(x, y, [[leftNeighbor, d, k], [rightNeighbor, d, k]], m, air)
        self.d = d
        self.k = k
        self.g = 3000
        self.cut = False

    def drawItems(self):
        items = []

        if self.getLeft() is not None:
            leftx = self.getLeft().x
            lefty = self.getLeft().y
            items.append(['line', self.x, self.y, leftx, lefty, "yellow"])

        if self.getRight() is not None:
            rightx = self.getRight().x
            righty = self.getRight().y
            items.append(['line', self.x, self.y, rightx, righty, "yellow"])

        items.append(['circle', self.x, self.y, 3, "yellow", 100])
        return items
        
    def getLeft(self):
        return self.connections[0][0]
    
    def getRight(self):
        return self.connections[1][0]
    
    def getdk(self):
        return self.d, self.k
    
    def setLeft(self, leftObject):
        self.connections[0] = [leftObject, self.d, self.k]
    
    def setRight(self, rightObject):
        self.connections[1] = [rightObject, self.d, self.k]

    def setLeftDist(self, newDist):
        self.connections[0][1] = newDist

    def setRightDist(self, newDist):
        self.connections[1][1] = newDist
    