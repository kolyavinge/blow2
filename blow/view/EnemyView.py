# -*- coding: utf-8 -*-

class EnemyView(object):
    
    def __init__(self, enemy, offsetX, q, enemySprite):
        self.enemy = enemy
        self.offsetX = offsetX
        self.q = q
        self.enemySprite = enemySprite
        self.enemySprite.scale = (q * enemy.getWidth()) / float(enemySprite.width)
    
    def draw(self):
        if not self.enemy.isDestroyed():
            self.enemySprite.x = self.offsetX + self.q * self.enemy.getX()
            self.enemySprite.y = self.q * self.enemy.getY()
            self.enemySprite.draw()
