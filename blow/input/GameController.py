# -*- coding: utf-8 -*-

class GameController(object):
    
    def __init__(self, game, view):
        self.game = game
        self.view = view
    
    def moveCar(self, dx):
        self.game.getWorld().getCar().move(dx)
    
    def moveExplosion(self, dx):
        self.game.getWorld().getExplosion().move(dx)
    
    def prevExplosionVolume(self):
        self.game.getWorld().getExplosion().setPrevVolume()
    
    def nextExplosionVolume(self):
        self.game.getWorld().getExplosion().setNextVolume()
    
    def blow(self):
        self.game.getWorld().getExplosion().blow()
        print self.game.getWorld().getExplosion().getPosition()
        
    def nextWorld(self):
        self.game.nextWorld()
    
    def resetWorld(self):
        self.game.resetWorld()

