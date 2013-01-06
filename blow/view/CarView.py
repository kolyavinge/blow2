# -*- coding: utf-8 -*-

import math

class CarView(object):
    
    def __init__(self, car, offsetX, q, carSprite):
        self.car = car
        self.offsetX = offsetX
        self.q = q
        self.carSprite = carSprite
        self.carSprite.scale = (q * car.getWidth()) / float(carSprite.width)
    
    def draw(self):
        self.carSprite.x = self.offsetX + self.q * self.car.getX()
        self.carSprite.y = self.q * self.car.getY()
        self.carSprite.rotation = 360.0 - math.degrees(self.car.getAngle())
        self.carSprite.draw()
