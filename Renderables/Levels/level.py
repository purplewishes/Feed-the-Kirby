from Renderables.Renderables import Renderable

class Level1(Renderable):

    def __init__(self):
        pass

    def getstep(self, mouseX, mouseY):
        if mouseX == None:
            return [['image','../Images/Level1.png', 0, 0]], self
        elif distance(mouseX, mouseY, 95, 725) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0]], None
        
        return [['image','../Images/Level1.png', 0, 0]], self
    
    
class Level2(Renderable):

    def __init__(self):
        pass

    def getstep(self, mouseX, mouseY):
        if mouseX == None:
            return [['image','../Images/Level2.png', 0, 0]], self
        elif distance(mouseX, mouseY, 90, 735) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0]], None
        
        return [['image','../Images/Level2.png', 0, 0]], self
    
class Level3(Renderable):

    def __init__(self):
        pass

    def getstep(self, mouseX, mouseY):
        if mouseX == None:
            return [['image','../Images/Level3.png', 0, 0]], self
        elif distance(mouseX, mouseY, 95, 725) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0]], None
        
        return [['image','../Images/Level3.png', 0, 0]], self
    
class Level4(Renderable):

    def __init__(self):
        pass

    def getstep(self, mouseX, mouseY):
        if mouseX == None:
            return [['image','../Images/Level4.png', 0, 0]], self
        elif distance(mouseX, mouseY, 95, 725) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0]], None
        
        return [['image','../Images/Level4.png', 0, 0]], self
    
def distance(x0, y0, x1, y1):
        return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5