# -*- coding: utf-8 -*-

import math

class CarView(object):
    
    def __init__(self, car, offsetX, sizeFactor, carSprite):
        self.car = car
        self.offsetX = offsetX
        self.sizeFactor = sizeFactor
        self.carSprite = carSprite
        self.carSprite.image.anchor_x = self.carSprite.image.width / 2.0
        self.carSprite.image.anchor_y = self.carSprite.image.height / 2.0
        self.carSprite.scale = (sizeFactor * car.getWidth()) / float(carSprite.width)
    
    def draw(self):
        self.carSprite.x = self.offsetX + self.sizeFactor * self.car.getCenterX()
        self.carSprite.y = self.sizeFactor * self.car.getCenterY()
        # у этого извращенского спрайта rotation в градусах и по часовой стрелке
        self.carSprite.rotation = 360.0 - math.degrees(self.car.getAngle())
        self.carSprite.draw()
