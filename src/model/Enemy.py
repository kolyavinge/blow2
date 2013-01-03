from model.GameObject import *

class Enemy(GameObject):
    
    def __init__(self, x, y, width, height):
        super(Enemy, self).__init__(x, y, width, height)
        self.destroyed = False
        
    def isDestroyed(self):
        return self.destroyed
    
    def destroy(self):
        self.destroyed = True