import math

EPSILON = 0.000001

class Object:

    def __init__(self, x, y, connections, mass, airResistance):
        self.x = x
        self.y = y
        self.connections = connections
        self.mass = mass
        self.airResistance = airResistance
        self.yvelocity = 0
        self.xvelocity = 0
        self.ticktime = 0.01
        self.g = 5000

    def calculateStep(self):
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
        
        #print(xforce, yforce)

        #updates velocity
        self.xvelocity += (xforce / self.mass) * self.ticktime 
        self.yvelocity += (yforce / self.mass) * self.ticktime
    
    def step(self):
        self.x += self.xvelocity * self.ticktime
        self.y += self.yvelocity * self.ticktime

    def disconnect(self, object):
        for i in range(len(self.connections)):
            if self.connections[i][0] is object:
                self.connections[i][0] = None
    
    def drawItems(self):
        pass