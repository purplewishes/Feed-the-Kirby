#Citations:
'''Utilized Linear Algebra to find out if the rope was cut, 
 researched this online before implementation'''

from Renderables.Renderables import Renderable
from Renderables.EndGame.endGame import EndGame
from Renderables.Levels.Objects.rope import RopeSegment
from Renderables.Levels.Objects.bubble import Bubble
from Renderables.Levels.Objects.kirby import Kirby
from Renderables.Levels.Objects.anchor import Anchor
from Renderables.Levels.Objects.point import Point
from Renderables.Levels.Objects.star import Star
from Renderables.Levels.Objects.spikes import Spikes


def distance(x0, y0, x1, y1):
    return ((x0 - x1) ** 2 + (y0 - y1) ** 2) ** 0.5

def createRope(length, numropes, anchor, star):
    x0 = anchor.x
    x1 = star.x
    y0 = anchor.y
    y1 = star.y

    rope = []
    #adds anchor
    previous = anchor
    d = (length / (numropes + 2)) * 0.2

    #adds all segments of ropes
    for i in range(numropes):
        x = x0 + (i + 1) * (x1 - x0) / numropes
        y = y0 + (i + 1) * (y1 - y0) / numropes
        ropenew = (RopeSegment(x, y, previous, None, d=d))

        #ignores anchor
        if i != 0:
            previous.setRight(ropenew)
        
        else:
            d, k = ropenew.getdk()
            previous.connections.append([ropenew, d, k])

        previous = ropenew
        rope.append(ropenew)

    #adds star
    previous.setRight(star)
    star.connections.append([previous, d, k])
    star.anchors.append([anchor, length])

    return rope

class Level(Renderable):
    def __init__(self, objects, points, level=0, spikes=[]):
        self.objects = objects
        self.prevMouseX = None
        self.prevMouseY = None
        self.points = points
        self.pointcount = 0
        self.spikes = spikes
        self.level = level

    def getStep(self, mouseX, mouseY):
        if mouseX != None and distance(mouseX, mouseY, 65, 745) <= 35:
            return [['image', '../Images/MainPage.png', 0, 0, 650, 800]], None
        
        if self.level == 3:
            drawables = [['image','../Images/Level3.png', 0, 0, 650, 800]]
            
        elif self.level == 1:
            drawables = [['image','../Images/Level1.png', 0, 0, 650, 800]]

        elif self.level == 4:
            drawables = [['image','../Images/Level4.png', 0, 0, 650, 800]]
        
        else:
            drawables = [['image','../Images/Background.png', 0, 0, 650, 800]]

        for object in self.objects:
            object.calculateStep()

        for object in self.objects:
            object.step()

        #saves kirby and star for future use
        for object in self.objects:
            if isinstance(object, Star):
                star = object
            if isinstance(object, Kirby):
                kirby = object
            
        #cut rope feature
        if mouseX != None:
            for object in self.objects:
                if isinstance(object, RopeSegment) and (not object.cut) and object.getLeft() != None and object.getRight() != None:
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
                                currentObject.mass = 1000
                                currentObject.yvelocity = 0
                                currentObject.xvelocity = 0

                            currentObject = currentObject.getLeft()

                        anchor = currentObject.getLeft()
                        
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
                                currentObject.mass = 1000
                                currentObject.yvelocity = 0
                                currentObject.xvelocity = 0

                            currentObject = currentObject.getRight()

                        star = currentObject.getRight()
                        
                        if currentObject.getRight() != None:
                            currentObject.getRight().disconnect(currentObject)
                        currentObject.setRight(None)

                        #cuts rope segment
                        if object.getLeft() != None:
                            object.getLeft().disconnect(object)
                        object.setLeft(None)

                        if anchor != None and star != None:
                            star.removeAnchor(anchor)

                        break

        #Tests if the star gathers points:
        for point in self.points:
            if distance(star.x, star.y, point.x, point.y) <= 30:
                self.pointcount += 1
                self.points.remove(point)
                #removes point from list of objects
                for object in self.objects:
                    if object is point:
                        self.objects.remove(point)
                        
        #adds objects to be drawed
        for object in self.objects:
            drawables += object.drawItems()

        #checks collisions with spikes
        if len(self.spikes) != 0:
            if (star.x >= 160 and star.x <= 290) and (star.y >= 510 and star.y <= 525): 
                return drawables, EndGame(self.pointcount, drawables, True)
            
            if (star.x >= 160 and star.x <= 290) and (star.y >= 360 and star.y <= 375):
                return drawables, EndGame(self.pointcount, drawables, True)

        #tests to see if game ended                
        if distance(star.x, star.y, kirby.x + 75, kirby.y + 75) <= 80:
            return drawables, EndGame(self.pointcount, drawables, False)

        if star.x > 650 or star.x < 0 or star.y > 800 or star.y < 0:
            return drawables, EndGame(self.pointcount, drawables, True)
        
        

        self.prevMouseX, self.prevMouseY = mouseX, mouseY
        return drawables, self
    
    
    

class Level1(Level):

    def __init__(self):
        objects = []

        anchor1 = Anchor(100, 0)
        star = Star(150, 100, [])
        anchor2 = Anchor(300, 0)
        anchor3 = Anchor(475, 0)

        point1 = Point(175, 380)
        point2 = Point(175, 625)
        point3 = Point(475, 380)

        kirby = Kirby(400, 600)

        points = [point1, point2, point3]

        objects += [kirby]
        objects += createRope(200, 7, anchor1, star) 
        objects += createRope(400, 6, anchor2, star)
        objects += createRope(700, 10, anchor3, star)

        objects += [anchor1, anchor2, point1, point2, point3, star, anchor3]
        super().__init__(objects, points, 1)
    
    
class Level2(Level):

    def __init__(self):
        objects = []
        points= []

        anchor1 = Anchor(150, 200)
        star = Star(150, 250, [])
        self.star = star
        anchor2 = Anchor(475, 400)
        point1 = Point(175, 500)
        point2 = Point(475, 75)
        point3 = Point(475, 250)
        bubble = Bubble(125, 575)
        self.bubble = bubble

        kirby = Kirby(400, 600)

        points = [point1, point2, point3]

        objects += [kirby]
        objects += createRope(200, 7, anchor1, star) 
        objects += createRope(350, 10, anchor2, star)

        objects += [anchor1, star, point1, point2, point3, anchor2, bubble]
        super().__init__(objects, points)

    def getStep(self, mouseX, mouseY):
        if self.bubble != None and distance(self.bubble.x, self.bubble.y, self.star.x, self.star.y) <= 100:
            self.objects.remove(self.bubble)
            self.star.inBubble = True
            self.bubble = None

        if self.star.inBubble and mouseX != None and distance(mouseX, mouseY, self.star.x, self.star.y) < 50:
            self.star.inBubble = False
        
        return super().getStep(mouseX, mouseY)
    
class Level3(Level):

    def __init__(self):
        self.objects = []
        points= []

        anchor1 = Anchor(100, 100)
        self.star = Star(100, 200, [])
        anchor2 = Anchor(180, 325)
        anchor3 = Anchor(295, 430)
        anchor4 = Anchor(420, 525)

        self.anchors = [[anchor2, False], [anchor3, False], [anchor4, False]]

        point1 = Point(180, 450)
        point2 = Point(295, 550)
        point3 = Point(420, 625)
       

        kirby = Kirby(400, 600)

        points = [point1, point2, point3]

        self.objects += [kirby]
        self.objects += createRope(100, 7, anchor1, self.star) 

        self.objects += [anchor1, self.star, point1, point2, point3, anchor2, anchor3, anchor4]
        super().__init__(self.objects, points, 3)

    def getStep(self, mouseX, mouseY):
        for anchor in self.anchors:
            if anchor[1] != True and distance(self.star.x, self.star.y, anchor[0].x, anchor[0].y) <= 90:
                self.objects += createRope(100, 7, anchor[0], self.star)
                anchor[1] = True 
                for object in self.objects:
                    if isinstance(object, Star):
                        self.objects.remove(object)
                        self.objects.append(object)

        return super().getStep(mouseX, mouseY)

    
class Level4(Level):

    def __init__(self):
        objects = []

        anchor1 = Anchor(100, 100)
        self.star = Star(150, 100, [])
        anchor2 = Anchor(325, 100)
        anchor3 = Anchor(325, 250)
        anchor4 = Anchor(325, 425)

        point1 = Point(130, 400)
        point2 = Point(130, 600)
        point3 = Point(500, 400)

        kirby = Kirby(250, 600)
        self.spike1 = Spikes(225, 450)
        self.spike2 = Spikes(225, 300)

        spikes = [self.spike1, self.spike2]

        points = [point1, point2, point3]

        objects += [kirby]
        objects += createRope(200, 7, anchor1, self.star) 
        objects += createRope(300, 7, anchor2, self.star)
        objects += createRope(220, 7, anchor3, self.star)
        objects += createRope(250, 7, anchor4, self.star)

        objects += [anchor1, anchor2, point1, point2, point3, self.star, anchor3, self.spike1, self.spike2, anchor4]
        super().__init__(objects, points, 4, spikes)