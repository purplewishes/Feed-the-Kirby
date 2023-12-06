#Citations:
 #Main Image of Kirby: https://kirby.miraheze.org/wiki/The_Kirby_Encyclopedia
    #Used in the levels, the main page, and the winning page
 #Image of Sad Kirby: https://www.deviantart.com/zmcdonald09/art/Kirby-Sad-933569584
    #Used in the game over you lost screen

from Renderables.Levels.object import Object

class Kirby(Object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def step(self):
        pass

    def calculateStep(self):
        pass

    def drawItems(self):
        return [['image', '../Images/Kirby.png', self.x, self.y, 160, 160]]