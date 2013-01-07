from blow.model.World import WorldError
from blow.model.Explosion import *
from blow.model.WorldBuilder import *
import unittest

class WorldBuilderTest(unittest.TestCase):
    
    def assertCarY(self, y, left, right):
        self.assertTrue(left <= y and y <= right, '{0} <= {1} <= {2}'.format(left, y, right))

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

    def testEnemyOutOfWorld(self):
        builder = WorldBuilder()
        builder.setSize(10, 20)
        self.assertRaises(WorldError, lambda: builder.addEnemy(-1, 5, 1, 2))
        self.assertRaises(WorldError, lambda: builder.addEnemy(1, -5, 1, 2))
        self.assertRaises(WorldError, lambda: builder.addEnemy(9, 5, 2, 2))
        self.assertRaises(WorldError, lambda: builder.addEnemy(1, 19, 1, 2))

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
        minX = min(carXPositions)
        self.assertTrue(minX > 0)
        
    def testHightExplosion(self):
        builder = WorldBuilder()
        builder.setSize(20, 100)
        world = builder.buildWorld()
        world.getExplosion().setVolume(ExplosionVolume_Hight)
        world.getExplosion().blow()
        carY = []
        for _ in range(0, 1000):
            world.update()
            carY.append(world.getCar().getY())
        maxCarY = max(carY)
        self.assertCarY(maxCarY, 15.0, 20.0)
        
    def testNormalExplosion(self):
        builder = WorldBuilder()
        builder.setSize(20, 100)
        world = builder.buildWorld()
        world.getExplosion().setVolume(ExplosionVolume_Normal)
        world.getExplosion().blow()
        carY = []
        for _ in range(0, 1000):
            world.update()
            carY.append(world.getCar().getY())
        maxCarY = max(carY)
        self.assertCarY(maxCarY, 8.0, 15.0)
    
    def testLowExplosion(self):
        builder = WorldBuilder()
        builder.setSize(20, 100)
        world = builder.buildWorld()
        world.getExplosion().setVolume(ExplosionVolume_Low)
        world.getExplosion().blow()
        carY = []
        for _ in range(0, 1000):
            world.update()
            carY.append(world.getCar().getY())
        maxCarY = max(carY)
        self.assertCarY(maxCarY, 6.0, 8.0)
        
    def testEnemyDestroy(self):
        builder = WorldBuilder()
        builder.setSize(10, 10)
        builder.addEnemy(5, 8, 1, 1)
        world = builder.buildWorld()
        world.getExplosion().setVolume(ExplosionVolume_Hight)
        world.getExplosion().blow()
        for _ in range(0, 1000):
            world.update()
        self.assertTrue(world.allEnemiesDestroyed())
        self.assertEquals(1, world.getEnemiesCount())
        self.assertEquals(5, world.getEnemies()[0].getX())
        self.assertEquals(8, world.getEnemies()[0].getY())
        self.assertTrue(world.isCompleted())
        
    def testMoveCarInLeft(self):
        builder = WorldBuilder()
        builder.setSize(10, 10)
        world = builder.buildWorld()
        world.getCar().move(-100)
        self.assertEquals(0, world.getCar().getX())
    
    def testMoveCarInRight(self):
        builder = WorldBuilder()
        builder.setSize(10, 10)
        world = builder.buildWorld()
        world.getCar().move(100)
        self.assertEquals(8, world.getCar().getX())
        
    def testMoveExplosionInLeft(self):
        builder = WorldBuilder()
        builder.setSize(10, 10)
        world = builder.buildWorld()
        world.getExplosion().move(-100)
        self.assertEquals(4, world.getExplosion().getX())
        
    def testMoveExplosionInRight(self):
        builder = WorldBuilder()
        builder.setSize(10, 10)
        world = builder.buildWorld()
        world.getExplosion().move(100)
        self.assertEquals(6, world.getExplosion().getX())
