from Renderables.Renderables import Renderable
from Renderables.Levels.Objects.rope import RopeSegment
from Renderables.Levels.Objects.bubble import Bubble
from Renderables.Levels.Objects.kirby import Kirby
from Renderables.Levels.Objects.anchor import Anchor
from Renderables.Levels.Objects.point import Point
from Renderables.Levels.Objects.star import Star
from Renderables.Levels.Objects.spikes import Spikes

def distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

def createRope(numropes, connect0, connect1):
    x0 = connect0.x
    x1 = connect1.x
    y0 = connect0.y
    y1 = connect1.y

    rope = []
    #adds anchor
    previous = connect0

    #adds all segments of ropes
    for i in range(numropes): 
        x = x0 + (i + 1) * (x1 - x0) / numropes
        y = y0 + (i + 1) * (y1 - y0) / numropes
        ropenew = (RopeSegment(x, y, previous, None))

        #ignores anchor
        if i != 0:
            previous.setRight(ropenew)
        
        else:
            d, k = ropenew.getdk()
            previous.connections.append([ropenew, d, k])

        previous = ropenew
        rope.append(ropenew)

    #adds star
    previous.setRight(connect1)
    connect1.connections.append([previous, d, k])

    return rope

class Level(Renderable):
    def __init__(self, objects):
        self.objects = objects
        self.prevMouseX = None
        self.prevMouseY = None

    def getstep(self, mouseX, mouseY):
        if mouseX != None and distance(mouseX, mouseY, 95, 725) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0, 650, 800]], None
        
        drawables = [['image','../Images/Background.png', 0, 0, 650, 800]]

        for object in self.objects:
            object.calculateStep()

        for object in self.objects:
            object.step()

        for object in self.objects:
            drawables += object.drawItems()
            
         #cut rope feature
        if mouseX != None:
            for object in self.objects:
                if isinstance(object, RopeSegment) and (not object.cut) and object.getLeft() != None and object.getRight() != None:
                    # dleftMouse = distance(mouseX, mouseY, object.getLeft().x, object.getLeft().y)
                    # dleft = distance(object.getLeft().x, object.getLeft().y, object.x, object.y)
                    # drightMouse = distance(mouseX, mouseY, object.getRight().x, object.getRight().y)
                    # dright = distance(object.getRight().x, object.getRight().y, object.x, object.y)
                    # dcenterMouse = distance(mouseX, mouseY, object.x, object.y)

                    # isHit = (dleftMouse + dcenterMouse < dleft + 20) or (drightMouse + dcenterMouse < dright + 20)

                    def ccw(A, B, C):
                        return (C[1]-A[1]) * (B[0]-A[0]) > (B[1]-A[1]) * (C[0]-A[0])

                    def intersect(A, B, C, D):
                        return ccw(A, C, D) != ccw(B, C, D) and ccw(A, B, C) != ccw(A, B, D)
                    
                    isHit = self.prevMouseX != None and (intersect([mouseX, mouseY], [self.prevMouseX, self.prevMouseY], [object.getLeft().x, object.getLeft().y], [object.x, object.y]) or \
                            intersect([mouseX, mouseY], [self.prevMouseX, self.prevMouseY], [object.getRight().x, object.getRight().y], [object.x, object.y]))

                    if isHit:
                        #cuts leftmost object
                        currentObject = object
                        while isinstance(currentObject.getLeft(), RopeSegment):
                            currentObject.cut = True
                            if currentObject.getLeft() != None and currentObject.getRight() != None:
                                dleftCur = distance(currentObject.getLeft().x, currentObject.getLeft().y, currentObject.x, currentObject.y)
                                currentObject.setLeftDist(dleftCur)
                                drightCur = distance(currentObject.getRight().x, currentObject.getRight().y, currentObject.x, currentObject.y)
                                currentObject.setRightDist(drightCur)
                                currentObject.g = 10000

                            currentObject = currentObject.getLeft()
                        
                        if currentObject.getLeft() != None:
                            currentObject.getLeft().disconnect(currentObject)
                        currentObject.setLeft(None)

                        #cuts rightmost object
                        currentObject = object
                        while isinstance(currentObject.getRight(), RopeSegment):
                            currentObject.cut = True
                            if currentObject.getLeft() != None and currentObject.getRight() != None:
                                dleftCur = distance(currentObject.getLeft().x, currentObject.getLeft().y, currentObject.x, currentObject.y)
                                currentObject.setLeftDist(dleftCur)
                                drightCur = distance(currentObject.getRight().x, currentObject.getRight().y, currentObject.x, currentObject.y)
                                currentObject.setRightDist(drightCur)
                                currentObject.g = 10000

                            currentObject = currentObject.getRight()
                        
                        if currentObject.getRight() != None:
                            currentObject.getRight().disconnect(currentObject)
                        currentObject.setRight(None)

                        #cuts rope segment
                        if object.getLeft() != None:
                            object.getLeft().disconnect(object)
                        object.setLeft(None)


                        break

        self.prevMouseX, self.prevMouseY = mouseX, mouseY
        return drawables, self
    
    
    

class Level1(Level):

    def __init__(self):
        objects = []

        anchor1 = Anchor(100, 0)
        star = Star(100, 100)
        anchor2 = Anchor(300, 0)
        anchor3 = Anchor(475, 0)

        objects += createRope(7, anchor1, star) 
        objects += createRope(15, anchor2, star)
        objects += createRope(20, anchor3, star)

        objects += [anchor1, anchor2, star, anchor3]
        super().__init__(objects)
    
    
class Level2(Renderable):

    def __init__(self):
        pass

    def getstep(self, mouseX, mouseY):
        if mouseX == None:
            return [['image','../Images/Level2.png', 0, 0, 650, 800]], self
        elif distance(mouseX, mouseY, 90, 735) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0, 650, 800]], None
        
        return [['image','../Images/Level2.png', 0, 0, 650, 800]], self
    
class Level3(Renderable):

    def __init__(self):
        pass

    def getstep(self, mouseX, mouseY):
        if mouseX == None:
            return [['image','../Images/Level3.png', 0, 0, 650, 800]], self
        elif distance(mouseX, mouseY, 95, 725) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0, 650, 800]], None
        
        return [['image','../Images/Level3.png', 0, 0, 650, 800]], self
    
class Level4(Renderable):

    def __init__(self):
        pass

    def getstep(self, mouseX, mouseY):
        if mouseX == None:
            return [['image','../Images/Level4.png', 0, 0, 650, 800]], self
        elif distance(mouseX, mouseY, 95, 725) <= 70:
            return [['image', '../Images/MainPage.png', 0, 0, 650, 800]], None
        
        return [['image','../Images/Level4.png', 0, 0, 650, 800]], self
    
def distance(x0, y0, x1, y1):
        return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5