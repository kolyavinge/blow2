import unittest
from model.Car import *
from model.Enemy import *
from model.Explosion import *
from model.World import *

class WorldTest(unittest.TestCase):

    def testConstructor(self):
        box2dWorld = StubBox2dWorld()
        car = Car(StubBox2dCarBody(), None)
        enemy1 = Enemy(0, 5, 1, 1)
        enemy2 = Enemy(5, 8, 1, 1)
        enemies = [enemy1, enemy2]
        explosion = Explosion(1)
        world = World(10, 20, box2dWorld, car, enemies, explosion)
        self.assertEquals(10, world.getWidth())
        self.assertEquals(20, world.getHeight())
        self.assertEquals(car, world.getCar())
        self.assertEquals(enemies, world.getEnemies())
        self.assertEquals(2, world.getEnemiesCount())
        self.assertEquals(explosion, world.getExplosion())
        self.assertFalse(world.isCompleted())

    def testAllEnemiesDestroyed(self):
        box2dWorld = StubBox2dWorld()
        car = Car(StubBox2dCarBody(), None)
        enemy1 = Enemy(0, 5, 1, 1)
        enemy2 = Enemy(5, 8, 1, 1)
        enemies = [enemy1, enemy2]
        explosion = Explosion(1)
        world = World(10, 20, box2dWorld, car, enemies, explosion)
        self.assertFalse(world.allEnemiesDestroyed())
        enemy1.destroy()
        self.assertFalse(world.allEnemiesDestroyed())
        enemy2.destroy()
        self.assertTrue(world.allEnemiesDestroyed())

    def testWorldUpdate(self):
        box2dWorld = StubBox2dWorld()
        car = Car(StubBox2dCarBody(), None)
        enemy1 = Enemy(0, 5, 1, 1)
        enemy2 = Enemy(5, 8, 1, 1)
        enemies = [enemy1, enemy2]
        explosion = Explosion(1)
        world = World(10, 20, box2dWorld, car, enemies, explosion)
        self.assertFalse(box2dWorld.StepCall)
        world.update()
        self.assertTrue(box2dWorld.StepCall)

class StubBox2dWorld(object):
    
    def __init__(self):
        self.StepCall = False
    
    def Step(self, a, b, c):
        self.StepCall = True

class StubBox2dCarBody(object):
    
    def GetPosition(self):
        return (5, 0)
    
    def ApplyForce(self, vector, position):
        self.vector = vector
        self.position = position

