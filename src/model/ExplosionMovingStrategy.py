class ExplosionMovingStrategy(object):
    
    def __init__(self, car):
        self.car = car
        
    def moveExplosion(self, explosion, dx):
        newX = explosion.getX() + dx
        
        if newX < self.car.getX():
            newX = self.car.getX()
        elif newX > self.car.getX() + self.car.getWidth():
            newX = self.car.getX() + self.car.getWidth()
            
        explosion.setX(newX)
