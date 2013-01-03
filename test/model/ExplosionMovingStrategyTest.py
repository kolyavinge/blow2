import unittest
from model.GameObject import *
from model.ExplosionMovingStrategy import *

class ExplosionMovingStrategyTest(unittest.TestCase):
    
    def testMoveExplosion(self):
        car = GameObject(1, 0, 2, 1)
        ms = ExplosionMovingStrategy(car)
        explosion = StubExplosion(2)
        ms.moveExplosion(explosion, 1)
        self.assertEquals(3, explosion.getX())
    
    def testMoveExplosionLeftOutOfCar(self):
        car = GameObject(1, 0, 2, 1)
        ms = ExplosionMovingStrategy(car)
        explosion = StubExplosion(2)
        ms.moveExplosion(explosion, -5)
        self.assertEquals(1, explosion.getX())
    
    def testMoveExplosionRightOutOfCar(self):
        car = GameObject(1, 0, 2, 1)
        ms = ExplosionMovingStrategy(car)
        explosion = StubExplosion(2)
        ms.moveExplosion(explosion, 5)
        self.assertEquals(3, explosion.getX())
        
class StubExplosion(object):
    
    def __init__(self, x):
        self.x = x
        
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x
