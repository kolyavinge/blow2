# -*- coding: utf-8 -*-

from blow.model.World import *

class WorldView(object):
    
    def __init__(self, world, offsetX, sizeFactor, backgroundImage, wallImage, childViews):
        self.world = world
        self.offsetX = offsetX
        self.sizeFactor = sizeFactor
        self.backgroundImage = backgroundImage
        self.wallImage = wallImage
        self.childViews = childViews
    
    def draw(self):
        self.backgroundImage.blit(0, 0, 0)
        self.drawChildViews()
        self.drawWalls()
    
    def drawWalls(self):
        height = self.sizeFactor * self.world.getHeight()
        x1 = self.offsetX - self.wallImage.width
        x2 = self.offsetX + self.sizeFactor * self.world.getWidth()
        y = 0
        while y < height:
            self.wallImage.blit(x1, y, 0)
            self.wallImage.blit(x2, y, 0)
            y += self.wallImage.height
    
    def drawChildViews(self):
        for view in self.childViews:
            view.draw()
