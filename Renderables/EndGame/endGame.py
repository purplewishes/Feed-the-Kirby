from Renderables.Renderables import Renderable
from Renderables.utils import distance

class EndGame(Renderable):
    def __init__(self, points, drawables, lost):
        self.drawables = drawables
        self.endscreens = ['../Images/YouWon0Stars.png', '../Images/YouWon1Star.png', '../Images/YouWon2Stars.png', '../Images/YouWon3Stars.png']
        self.points = points
        self.lost = lost

    def getStep(self, mouseX, mouseY): 
        if self.lost:
            self.drawables += [['image','../Images/YouLost.png', 0, 0, 650, 800]]
        else:
            self.drawables += [['image', self.endscreens[self.points], 0, 0, 650, 800]]
        
        if mouseX != None and (distance(mouseX, mouseY, 160, 615) <= 30 \
            or distance(mouseX, mouseY, 65, 745) <= 35):
            return [['image', '../Images/MainPage.png', 0, 0, 650, 800]], None

        else: 
            return self.drawables, self