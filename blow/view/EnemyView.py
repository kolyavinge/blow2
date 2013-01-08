# -*- coding: utf-8 -*-

class EnemyView(object):
    
    def __init__(self, enemy, offsetX, sizeFactor, enemySprite):
        self.enemy = enemy
        self.offsetX = offsetX
        self.sizeFactor = sizeFactor
        self.enemySprite = enemySprite
        self.enemySprite.scale = (sizeFactor * enemy.getWidth()) / float(enemySprite.width)
    
    def draw(self):
        if not self.enemy.isDestroyed():
            self.enemySprite.x = self.offsetX + self.sizeFactor * self.enemy.getX()
            self.enemySprite.y = self.sizeFactor * self.enemy.getY()
            self.enemySprite.draw()
