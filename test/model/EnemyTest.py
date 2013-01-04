import unittest
from blow.model.Enemy import *

class EnemyTest(unittest.TestCase):

    def testConstructor(self):
        enemy = Enemy(1, 2, 10, 20)
        self.assertEquals(1, enemy.getX())
        self.assertEquals(2, enemy.getY())
        self.assertEquals(10, enemy.getWidth())
        self.assertEquals(20, enemy.getHeight())
        self.assertFalse(enemy.isDestroyed())

    def testDestroy(self):
        enemy = Enemy(1, 2, 10, 20)
        self.assertFalse(enemy.isDestroyed())
        enemy.destroy()
        self.assertTrue(enemy.isDestroyed())
