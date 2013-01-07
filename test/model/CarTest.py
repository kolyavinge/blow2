import unittest
from blow.model.Car import *

class CarTest(unittest.TestCase):

    def testConstructor(self):
        body = StubBox2dCarBody()
        car = Car(body)
        self.assertEquals(4, car.getX())
        self.assertEquals(0, car.getY())
        self.assertEquals(2, car.getWidth())
        self.assertEquals(1, car.getHeight())
        self.assertFalse(car.isBlowed())
        
    def testMoveCar(self):
        body = StubBox2dCarBody()
        cms = StubCarMovingStrategy()
        car = Car(body)
        car.setMovingStrategy(cms)
        self.assertFalse(cms.moveCarCall)
        car.move(5)
        self.assertTrue(cms.moveCarCall)
        self.assertEquals(car, cms.car)
        self.assertEquals(5, cms.dx)
        
    def testBlow(self):
        body = StubBox2dCarBody()
        car = Car(body)
        vector = (0, 1)
        position = (1, 0)
        car.blow(vector, position)
        self.assertTrue(car.isBlowed())
        self.assertEquals((0, 1), body.vector)
        self.assertEquals(position, body.position)
        
    def testTwiceBlow(self):
        body = StubBox2dCarBody()
        car = Car(body)
        car.blow((0, 1), (1, 0))
        self.assertRaises(CarError, lambda: car.blow((1, 0), (1, 2)))
        
    def testMoveCarAfterBlow(self):
        car = Car(StubBox2dCarBody())
        car.setMovingStrategy(StubCarMovingStrategy())
        car.blow((0, 1), (1, 0))
        self.assertRaises(CarError, lambda: car.move(1))
        
    def testSetX(self):
        car = Car(StubBox2dCarBody())
        car.setX(4)
        self.assertEquals(4, car.getX())

class StubCarMovingStrategy(object):
    
    def __init__(self):
        self.moveCarCall = False
    
    def moveCar(self, car, dx):
        self.moveCarCall = True
        self.car = car
        self.dx = dx

class StubBox2dCarBody(object):
    
    def GetPosition(self):
        return (5.0, 0.5)
    
    def setPosition(self, pos):
        pass
    
    def GetMass(self):
        return 2.0
    
    def ApplyImpulse(self, vector, position):
        self.vector = vector
        self.position = position
        