import unittest
from blow.model.WorldBuilderUtils import buildWorldFromList

class WorldBuilderUtilsTest(unittest.TestCase):

    def testBuildWorldFromList(self):
        world = buildWorldFromList([(10, 20), [(1, 2, 3, 4), (5, 8, 1, 2)]])
        
        self.assertEquals(10, world.getWidth())
        self.assertEquals(20, world.getHeight())
        
        self.assertEquals(4, world.getCar().getX())
        self.assertEquals(0, world.getCar().getY())
        
        self.assertEquals(2, world.getEnemiesCount())
        
        self.assertEquals(1, world.getEnemies()[0].getX())
        self.assertEquals(2, world.getEnemies()[0].getY())
        self.assertEquals(3, world.getEnemies()[0].getWidth())
        self.assertEquals(4, world.getEnemies()[0].getHeight())
        
        self.assertEquals(5, world.getEnemies()[1].getX())
        self.assertEquals(8, world.getEnemies()[1].getY())
        self.assertEquals(1, world.getEnemies()[1].getWidth())
        self.assertEquals(2, world.getEnemies()[1].getHeight())

    def testBuildWorldFromList_WrongList(self):
        self.assertRaises(ValueError, lambda: buildWorldFromList([(10, 20)]))
        self.assertRaises(ValueError, lambda: buildWorldFromList([(10, 20, 30), []]))
        self.assertRaises(ValueError, lambda: buildWorldFromList([(10, 20), [(1, 2, 3, 4, 5)]]))
        self.assertRaises(ValueError, lambda: buildWorldFromList([(10, 20), [(1, 2, 3)]]))