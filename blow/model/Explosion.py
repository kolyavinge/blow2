ExplosionVolume_Low = 3.5
ExplosionVolume_Normal = 4.0
ExplosionVolume_Hight = 4.8

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
            vector = (0, self.volume)
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
    
    def getPosition(self):
        return (self.getX(), self.getY())
    
    def getVolume(self):
        return self.volume
    
    def setVolume(self, v):
        if not self.blowing:
            self.volume = v
        else:
            raise ExplosionError('you cant blow blowing explosion')
    
    def setPrevVolume(self):
        self.setVolume(self.__getPrevVolume())
    
    def setNextVolume(self):
        self.setVolume(self.__getNextVolume())

    def setMovingStrategy(self, movingStrategy):
        self.movingStrategy = movingStrategy
        
    def setBlowingObject(self, blowingObject):
        self.blowingObject = blowingObject
    
    def __getNextVolume(self):
        if self.volume == ExplosionVolume_Low:
            return ExplosionVolume_Normal
        elif self.volume == ExplosionVolume_Normal:
            return ExplosionVolume_Hight
        elif self.volume == ExplosionVolume_Hight:
            return ExplosionVolume_Low
        else:
            raise ExplosionError('undefine volume type: {0}'.format(self.volume))
    
    def __getPrevVolume(self):
        if self.volume == ExplosionVolume_Low:
            return ExplosionVolume_Hight
        elif self.volume == ExplosionVolume_Normal:
            return ExplosionVolume_Low
        elif self.volume == ExplosionVolume_Hight:
            return ExplosionVolume_Normal
        else:
            raise ExplosionError('undefine volume type: {0}'.format(self.volume))

class ExplosionError(RuntimeError):
    pass
