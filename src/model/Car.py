from model.GameObject import *

carWidth = 2.0
carHeight = 1.0

class Car(GameObject):

    def __init__(self, box2dCarBody, movingStrategy):
        self.box2dCarBody = box2dCarBody
        x = box2dCarBody.GetPosition()[0] - carWidth / 2.0
        super(Car, self).__init__(x, 0, carWidth, carHeight)
        self.movingStrategy = movingStrategy
        self.blowing = False
        
    def move(self, dx):
        if not self.blowing:
            self.movingStrategy.moveCar(self, dx)
        else:
            raise CarError('you cant move blowing car')
        
    def blow(self, vector, position):
        if not self.blowing:
            self.blowing = True
            self.box2dCarBody.ApplyForce(vector, position)
        else:
            raise CarError('you cant blow blowing car')

    def getAngle(self):
        return self.box2dCarBody.GetAngle()
    
    def getX(self):
        return self.box2dCarBody.GetPosition()[0] - self.getWidth() / 2.0
    
    def setX(self, x):
        x += carWidth / 2.0
        self.box2dCarBody.setPosition((x, carHeight / 2.0))
    
    def getY(self):
        return self.box2dCarBody.GetPosition()[1] - self.getHeight() / 2.0
    
    def isBlowed(self):
        return self.blowing
    
    def isSleeping(self):
        return self.box2dCarBody.IsSleeping()

class CarError(RuntimeError):
    pass
