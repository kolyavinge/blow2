import unittest
from model.GameObject import *
from model.Car import *
from model.CarMovingStrategy import CarMovingStrategy

class CarMovingStrategyTest(unittest.TestCase):

    def testMoveCar(self):
        car = StubCar(1, 0, 1, 1)
        worldWidth = 10
        explosion = StubExplosion(2)
        cms = CarMovingStrategy(worldWidth, explosion)
        cms.moveCar(car, 2)
        self.assertEquals(3, car.getX())
        self.assertEquals(4, explosion.x)
        
    def testMoveCarLeftOutOfWorld(self):
        car = StubCar(1, 0, 1, 1)
        worldWidth = 10
        explosion = StubExplosion(2)
        cms = CarMovingStrategy(worldWidth, explosion)
        cms.moveCar(car, -4)
        self.assertEquals(0, car.getX())
        self.assertEquals(1, explosion.x)
        
    def testMoveCarRightOutOfWorld(self):
        car = StubCar(8, 0, 1, 1)
        worldWidth = 10
        explosion = StubExplosion(2)
        cms = CarMovingStrategy(worldWidth, explosion)
        cms.moveCar(car, 5)
        self.assertEquals(9, car.getX())
        self.assertEquals(3, explosion.x)
        
class StubCar(GameObject):
    
    def __init__(self, x, y, width, height):
        super(StubCar, self).__init__(x, y, width, height)
        
    def setX(self, x):
        self.x = x

class StubExplosion(object):
    
    def __init__(self, x):
        self.x = x
        
    def move(self, dx):
        self.x += dx
