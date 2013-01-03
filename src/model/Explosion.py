ExplosionVolume_Low = 3.5
ExplosionVolume_Normal = 4.0
ExplosionVolume_Hight = 4.5

class Explosion(object):
    
    def __init__(self, x):
        self.x = x
        self.volume = ExplosionVolume_Normal
        self.blowing = False
        
    def move(self, dx):
        if not self.blowing:
            self.movingStrategy.moveExplosion(self, dx)
        else:
            raise ExplosionError('you cant move blowing explosion')
    
    def blow(self):
        if not self.blowing:
            self.blowing = True
            vector = (0, ExplosionVolume_Hight)
            position = (self.getX(), self.getY())
            self.blowingObject.blow(vector, position)
        else:
            raise ExplosionError('you cant blow blowing explosion')

    def isBlowing(self):
        return self.blowing
    
    def getX(self):
        return self.x
    
    def setX(self, x):
        self.x = x
    
    def getY(self):
        return 0
    
    def getVolume(self):
        return self.volume
    
    def setVolume(self, v):
        if not self.blowing:
            self.volume = v
        else:
            raise ExplosionError('you cant blow blowing explosion')

    def setMovingStrategy(self, movingStrategy):
        self.movingStrategy = movingStrategy
        
    def setBlowingObject(self, blowingObject):
        self.blowingObject = blowingObject    

class ExplosionError(RuntimeError):
    pass
