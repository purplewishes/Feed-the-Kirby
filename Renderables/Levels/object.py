import math
from Renderables.utils import distance, project
EPSILON = 0.000001

def threshold(x, th):
    if x > 0:
        return min(x, th)
    else:
        return max(x, -th)

class Object:

    def __init__(self, x, y, connections, mass, airResistance): #initializes physics
        self.x = x
        self.y = y
        self.connections = connections
        self.mass = mass
        self.airResistance = airResistance
        self.yvelocity = 0
        self.xvelocity = 0
        self.yforce = 0
        self.xforce = 0
        self.ticktime = 0.01
        self.g = 5000

        self.velMax = 6000
        self.stepMax = 30

    def calculateStep(self): #calculates actions for the step
        xforce = 0
        yforce = 0
        velocity = (self.xvelocity ** 2 + self.yvelocity ** 2) ** 0.5

        #calculating object forces
        for object, d, k in self.connections: 
            if object is None:
                continue
            dx = object.x - self.x
            dy = object.y - self.y
            da = (dx ** 2 + dy ** 2) ** 0.5 + EPSILON

            yforce += k * (da - d) * (dy / da) * ((abs(da - d)) ** (1))
            xforce += k * (da - d) * (dx / da) * ((abs(da - d)) ** (1))



        #factors in gravity
        yforce += self.mass * self.g 
        
        #factors in air resistance
        yforce -= self.airResistance * velocity * self.yvelocity 
        xforce -= self.airResistance * velocity * self.xvelocity
        
        self.xforce = xforce
        self.yforce = yforce
        
    
    def step(self): #takes a step
        #updates velocity
        self.xvelocity += (self.xforce / self.mass) * self.ticktime 
        self.yvelocity += (self.yforce / self.mass) * self.ticktime

        self.xvelocity = threshold(self.xvelocity, self.velMax)
        self.yvelocity = threshold(self.yvelocity, self.velMax)

        self.x += threshold(self.xvelocity * self.ticktime, self.stepMax)
        self.y += threshold(self.yvelocity * self.ticktime, self.stepMax)

        

    def disconnect(self, object):
        for i in range(len(self.connections)):
            if self.connections[i][0] is object:
                self.connections[i][0] = None
    
    def drawItems(self): #returns items to be drawn
        pass