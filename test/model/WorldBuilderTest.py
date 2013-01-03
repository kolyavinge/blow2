import unittest
from model.Explosion import *
from model.WorldBuilder import *

class WorldBuilderTest(unittest.TestCase):

    def testBuild(self):
        builder = WorldBuilder()
        builder.setSize(10, 20)
        builder.addEnemy(1, 5, 1, 2)
        builder.addEnemy(6, 8, 2, 1)
        
        world = builder.buildWorld()

        self.assertEquals(10, world.getWidth())
        self.assertEquals(20, world.getHeight())
        self.assertFalse(world.isCompleted())
        
        self.assertEquals(4, world.getCar().getX())
        self.assertEquals(0, world.getCar().getY())
#        self.assertTrue(world.getCar().isSleeping())
        self.assertFalse(world.getCar().isBlowed())
        
        self.assertEquals(5, world.getExplosion().getX())
        self.assertEquals(0, world.getExplosion().getY())
        self.assertEquals(ExplosionVolume_Normal, world.getExplosion().getVolume())
        
        self.assertEquals(2, world.getEnemiesCount())
        self.assertEquals(1, world.getEnemies()[0].getX())
        self.assertEquals(5, world.getEnemies()[0].getY())
        self.assertEquals(1, world.getEnemies()[0].getWidth())
        self.assertEquals(2, world.getEnemies()[0].getHeight())
        self.assertEquals(6, world.getEnemies()[1].getX())
        self.assertEquals(8, world.getEnemies()[1].getY())
        self.assertEquals(2, world.getEnemies()[1].getWidth())
        self.assertEquals(1, world.getEnemies()[1].getHeight())

    def testRightWall(self):
        builder = WorldBuilder()
        builder.setSize(20, 100)
        world = builder.buildWorld()
        world.getCar().move(9)
        world.getExplosion().setVolume(ExplosionVolume_Hight)
        world.getExplosion().move(-1)
        world.getExplosion().blow()
        carXPositions = []
        for _ in range(0, 100):
            world.update()
            carXPositions.append(world.getCar().getX())
        maxX = max(carXPositions)
        self.assertTrue(maxX < 20)
        
    def testLeftWall(self):
        builder = WorldBuilder()
        builder.setSize(20, 100)
        world = builder.buildWorld()
        world.getCar().move(-9)
        world.getExplosion().setVolume(ExplosionVolume_Hight)
        world.getExplosion().move(1)
        world.getExplosion().blow()
        carXPositions = []
        for _ in range(0, 100):
            world.update()
            carXPositions.append(world.getCar().getX())
        maxX = max(carXPositions)
        self.assertTrue(maxX > 0)
        
        