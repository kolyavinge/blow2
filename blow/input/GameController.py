# -*- coding: utf-8 -*-

class GameController(object):
    
    def __init__(self, game):
        self.game = game
    
    def moveCar(self, dx):
        if not self.game.getWorld().getCar().isBlowed():
            self.game.getWorld().getCar().move(dx)
    
    def moveExplosion(self, dx):
        if not self.game.getWorld().getExplosion().isBlowing():
            self.game.getWorld().getExplosion().move(dx)
    
    def prevExplosionVolume(self):
        if not self.game.getWorld().getExplosion().isBlowing():
            self.game.getWorld().getExplosion().setPrevVolume()
    
    def nextExplosionVolume(self):
        if not self.game.getWorld().getExplosion().isBlowing():
            self.game.getWorld().getExplosion().setNextVolume()
    
    def blow(self):
        if not self.game.getWorld().getExplosion().isBlowing():
            self.game.getWorld().getExplosion().blow()
        
    def nextWorld(self):
        if self.game.getWorld().isCompleted():
            self.game.nextWorld()
    
    def resetWorld(self):
        self.game.resetWorld()
