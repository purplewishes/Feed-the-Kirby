from Renderables.Renderables import Renderable
from Renderables.Levels.level import Level1, Level2, Level3, Level4

class MainPage(Renderable):
    def __init__(self):
        self.buttons = [(120, 460), (320, 510), (150, 640), (355, 695)]
        
        #buttons : (120, 460), (320, 510), (150, 640), (355, 695)
    
    def getstep(self, mouseX, mouseY):
        mainPageImage = [['image', '../Images/MainPage.png', 0, 0]]
        levels = [Level1(), Level2(), Level3(), Level4()]
        if mouseX == None: #if nothing is clicked return mainPage
            return mainPageImage, self
        else:
            for i in range(len(self.buttons)): #checks if buttons are clicked
                if self.distance(mouseX, mouseY, self.buttons[i][0], self.buttons[i][1]) <= 40:
                    return [], levels[i]
                
        return mainPageImage, self #returns if click is outside every button
        
    def distance(self, x0, y0, x1, y1):
        return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5
    