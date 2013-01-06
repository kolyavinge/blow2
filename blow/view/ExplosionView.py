# -*- coding: utf-8 -*-

from blow.model.Explosion import *

class ExplosionView(object):
    
    def __init__(self, explosion, offsetX, q, explosionSprite):
        self.explosion = explosion
        self.offsetX = offsetX
        self.q = q
        self.explosionSprite = explosionSprite
        self.z = self.q / float(self.explosionSprite.width)

    def draw(self):
        if not self.explosion.isBlowing():
            self.explosionSprite.scale = self.getVolumeFactor() * self.z
            self.explosionSprite.x = self.offsetX + self.q * self.explosion.getX() - self.explosionSprite.width / 2.0
            self.explosionSprite.y = self.q * self.explosion.getY()
            self.explosionSprite.draw()

    def getVolumeFactor(self):
        if self.explosion.getVolume() == ExplosionVolume_Low:
            return 0.5
        elif self.explosion.getVolume() == ExplosionVolume_Normal:
            return 0.8
        else: # ExplosionVolume_Hight
            return 1.0
