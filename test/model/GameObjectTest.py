import unittest
from blow.model.GameObject import *

class GameObjectTest(unittest.TestCase):

    def testConstructor(self):
        go = GameObject(1, 2, 10, 20)
        self.assertEquals(1, go.getX())
        self.assertEquals(2, go.getY())
        self.assertEquals(10, go.getWidth())
        self.assertEquals(20, go.getHeight())

    def testGetCenter(self):
        go = GameObject(1, 2, 10, 20)
        self.assertEquals(6, go.getCenterX())
        self.assertEquals(12, go.getCenterY())
