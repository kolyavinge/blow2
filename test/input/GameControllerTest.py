# -*- coding: utf-8 -*-

import unittest
from blow.model.Game import *
from blow.input.GameController import *

class GameControllerTest(unittest.TestCase):
    
    def setUp(self):
        self.game = Game([[(8, 9), []]])
        self.controller = GameController(self.game)
    
    def testMoveCarAfterBlow(self):
        x = self.game.getWorld().getCar().getX()
        self.controller.blow()
        self.controller.moveCar(-1.0)
        self.controller.moveCar(5.0)
        dx = self.game.getWorld().getCar().getX() - x
        self.assertEquals(0, dx)

    def testMoveExplosionAfterBlow(self):
        x = self.game.getWorld().getExplosion().getX()
        self.controller.blow()
        self.controller.moveExplosion(-2.0)
        self.controller.moveExplosion(8.0)
        dx = self.game.getWorld().getExplosion().getX() - x
        self.assertEquals(0, dx)
    
    def testChangeExplosionVolumeAfterBlow(self):
        volume = self.game.getWorld().getExplosion().getVolume()
        self.controller.blow()
        self.controller.nextExplosionVolume()
        self.assertEquals(volume, self.game.getWorld().getExplosion().getVolume())
        self.controller.prevExplosionVolume()
        self.assertEquals(volume, self.game.getWorld().getExplosion().getVolume())

    def testTwiceBlow(self):
        self.controller.blow()
        self.controller.blow()
        # no exception and errors !
