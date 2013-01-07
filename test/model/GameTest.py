from blow.model.Explosion import *
from blow.model.Game import *
import unittest

class GameTest(unittest.TestCase):

    def testGetFirstWorld(self):
        worlds = [[(15, 25), [(1, 2, 3, 4)]]]
        game = Game(worlds)
        self.assertEquals(GameState_Continue, game.getState())
        self.assertSize((15, 25), game.getWorld())

    def testResetWorld(self):
        game = Game([ [(10, 25), [(1, 10, 3, 4)]] ])
        game.getWorld().getCar().move(-100)
        game.getWorld().getExplosion().move(100)
        game.getWorld().getExplosion().setVolume(ExplosionVolume_Hight)
        game.getWorld().getExplosion().blow()
        self.manyUpdates(game.getWorld())
        
        game.resetWorld()
        
        self.assertSize((10, 25), game.getWorld())
        self.assertPosition((4, 0), game.getWorld().getCar())
        self.assertPosition((5, 0), game.getWorld().getExplosion())
        self.assertEquals(ExplosionVolume_Normal, game.getWorld().getExplosion().getVolume())
        self.assertEquals(1, game.getWorld().getEnemiesCount())
        self.assertPosition((1, 10), game.getWorld().getEnemies()[0])
        self.assertSize((3, 4), game.getWorld().getEnemies()[0])
        
    def testNextWorld(self):
        game = Game([ [(10, 20), [(5, 4, 1, 1)]], [(15, 25), [(5, 5, 1, 1)]] ])
        game.getWorld().getExplosion().blow()
        self.manyUpdates(game.getWorld())
        
        game.nextWorld()
        
        self.assertSize((15, 25), game.getWorld())
    
#    def testOnChangeWorld(self):
#        onChangeWorldCall = False
##        def onChangeWorld(world):
##            onChangeWorldCall = True
#        game = Game([ [(10, 20), []], [(10, 20), []] ])
#        game.onChangeWorld = lambda(world): onChangeWorldCall = True
#        game.getWorld().getExplosion().blow()
#        self.manyUpdates(game.getWorld())
#        self.assertFalse(onChangeWorldCall)
#        game.nextWorld()
#        self.assertTrue(onChangeWorldCall)
        
    def testNextWorldNonComplete(self):
        game = Game([ [(100, 20), [(1, 10, 1, 1)]] ])
        game.getWorld().getExplosion().blow()
        self.manyUpdates(game.getWorld())
        self.assertRaises(GameError, lambda: game.nextWorld())
    
    def testAllLevelsComplete(self):
        game = Game([ [(10, 20), [(5, 4, 1, 1)]] ])
        game.getWorld().getExplosion().blow()
        self.manyUpdates(game.getWorld())
        self.assertEquals(GameState_Continue, game.getState())
        game.nextWorld()
        self.assertEquals(GameState_AllLevelsCompleted, game.getState())
        
    def manyUpdates(self, world):
        for _ in range(0, 1000):
            world.update()
        
    def assertPosition(self, pos, obj):
        self.assertEquals(pos, (obj.getX(), obj.getY()))
        
    def assertSize(self, size, obj):
        self.assertEquals(size, (obj.getWidth(), obj.getHeight()))
        
        
        
