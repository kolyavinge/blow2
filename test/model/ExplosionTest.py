import unittest
from blow.model.GameObject import *
from blow.model.Explosion import *

class ExplosionTest(unittest.TestCase):

    def testConstructor(self):
        explosion = Explosion(2)
        self.assertEquals(2, explosion.getX())
        self.assertEquals(0, explosion.getY())
        self.assertEquals(ExplosionVolume_Normal, explosion.getVolume())
        self.assertFalse(explosion.isBlowing())
        
    def testGetSetVolume(self):
        explosion = Explosion(2)
        self.assertEquals(ExplosionVolume_Normal, explosion.getVolume())
        explosion.setVolume(ExplosionVolume_Low)
        self.assertEquals(ExplosionVolume_Low, explosion.getVolume())
    
    def testSetPrevVolume(self):
        explosion = Explosion(2)
        self.assertEquals(ExplosionVolume_Normal, explosion.getVolume())
        explosion.setPrevVolume()
        self.assertEquals(ExplosionVolume_Low, explosion.getVolume())
        explosion.setPrevVolume()
        self.assertEquals(ExplosionVolume_Hight, explosion.getVolume())
        explosion.setPrevVolume()
        self.assertEquals(ExplosionVolume_Normal, explosion.getVolume())
    
    def testSetNextVolume(self):
        explosion = Explosion(2)
        self.assertEquals(ExplosionVolume_Normal, explosion.getVolume())
        explosion.setNextVolume()
        self.assertEquals(ExplosionVolume_Hight, explosion.getVolume())
        explosion.setNextVolume()
        self.assertEquals(ExplosionVolume_Low, explosion.getVolume())
        explosion.setNextVolume()
        self.assertEquals(ExplosionVolume_Normal, explosion.getVolume())
    
    def testSetPrevVolumeOnBlowingExplosion(self):
        explosion = Explosion(2)
        explosion.setBlowingObject(StubBlowingObject())
        explosion.blow()
        self.assertRaises(ExplosionError, lambda: explosion.setPrevVolume())
        
    def testSetNextVolumeOnBlowingExplosion(self):
        explosion = Explosion(2)
        explosion.setBlowingObject(StubBlowingObject())
        explosion.blow()
        self.assertRaises(ExplosionError, lambda: explosion.setNextVolume())
        
    def testBlow(self):
        explosion = Explosion(1.5)
        blowingObject = StubBlowingObject()
        blowingObject.setPosition(1.0, 0.0)
        explosion.setBlowingObject(blowingObject)
        explosion.setVolume(ExplosionVolume_Hight)
        self.assertFalse(blowingObject.blowCall)
        explosion.blow()
        self.assertTrue(explosion.isBlowing())
        self.assertTrue(blowingObject.blowCall)
        self.assertEquals((0.0, ExplosionVolume_Hight), blowingObject.blowVector)
        self.assertEquals((1.5, 1.0), blowingObject.blowPosition)
        
    def testTwiceBlow(self):
        explosion = Explosion(2)
        explosion.setBlowingObject(StubBlowingObject())
        explosion.blow()
        self.assertRaises(ExplosionError, lambda: explosion.blow())
        
    def testSetVolumeOnBlowingExplosion(self):
        explosion = Explosion(2)
        explosion.setBlowingObject(StubBlowingObject())
        explosion.blow()
        self.assertRaises(ExplosionError, lambda: explosion.setVolume(ExplosionVolume_Normal))
        
    def testMove(self):
        ms = StubExplosionMovingStrategy()
        explosion = Explosion(2)
        explosion.setMovingStrategy(ms)
        self.assertFalse(ms.moveExplosionCall)
        explosion.move(5)
        self.assertTrue(ms.moveExplosionCall)
        self.assertEquals(explosion, ms.exlosion)
        self.assertEquals(5, ms.dx)
        
    def testMoveBowingExplosion(self):
        explosion = Explosion(2)
        explosion.setMovingStrategy(StubExplosionMovingStrategy())
        explosion.setBlowingObject(StubBlowingObject())
        explosion.blow()
        self.assertRaises(ExplosionError, lambda: explosion.move(1))
        
    def testSetX(self):
        explosion = Explosion(2)
        explosion.setX(4)
        self.assertEquals(4, explosion.getX())

class StubBlowingObject(GameObject):
    
    def __init__(self):
        super(StubBlowingObject, self).__init__(0.0, 0.0, 1.0, 1.0)
        self.blowCall = False
        
    def setPosition(self, x, y):
        self.x, self.y = x, y
    
    def blow(self, vector, position):
        self.blowCall = True
        self.blowVector, self.blowPosition = vector, position

class StubExplosionMovingStrategy(object):
    
    def __init__(self):
        self.moveExplosionCall = False
    
    def moveExplosion(self, explosion, dx):
        self.moveExplosionCall = True
        self.exlosion = explosion
        self.dx = dx
        
