#Citations:
 #The star used as candy to feed Kirby: https://pngtree.com/freepng/star-png-vector-icon-ui-game_8528046.html

import math
from Renderables.Levels.object import Object
from Renderables.utils import distance, project

class Star(Object):

    def __init__(self, x, y, anchors):
        super().__init__(x, y, [], 5, 0.001)
        self.anchors = anchors
        self.inBubble = False

    def drawItems(self):
        if self.inBubble:
            return [['image', '../Images/BubbleStar.png', self.x - 50, self.y - 50, 100, 100]]
        
        return [['image', '../Images/Star.png', self.x - 50, self.y - 50, 100, 100]]
    
    def calculateStep(self):
        if self.inBubble:
            self.g = -2000
            self.airResistance = 0.01
        else:
            self.g = 5000
            self.airResistance = 0.001
        
        super().calculateStep()

        for anchor, dist in self.anchors:
            if distance(self.x, self.y, anchor.x, anchor.y) >= dist:
                dx = anchor.x - self.x
                dy = anchor.y - self.y

                vxParallel, vyParallel = project(self.xvelocity, self.yvelocity, dx, dy)
                vxPerpen, vyPerpen = project(self.xvelocity, self.yvelocity, dy, -dx)

                antiFx, antiFy = project(self.xforce, self.yforce, dx, dy)
                if antiFx * dx < 0 or antiFy * dy < 0:
                    antiFx, antiFy = -antiFx, -antiFy
                else:
                    antiFx, antiFy = 0, 0

                centiMag = self.mass * (vxPerpen ** 2 + vyPerpen ** 2) / distance(self.x, self.y, anchor.x, anchor.y)
                centiFx = centiMag * dx / math.sqrt(dx ** 2 + dy ** 2)
                centiFy = centiMag * dy / math.sqrt(dx ** 2 + dy ** 2)

                self.xforce += antiFx + centiFx
                self.yforce += antiFy + centiFy
                if vxParallel * dx < 0 or vyParallel * dy < 0:
                    self.xvelocity = vxPerpen
                    self.yvelocity = vyPerpen

    def removeAnchor(self, anchor):
        for i in range(len(self.anchors)):
            if self.anchors[i][0] == anchor:
                self.anchors.pop(i)
                break


        
