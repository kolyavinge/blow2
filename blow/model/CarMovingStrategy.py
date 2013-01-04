class CarMovingStrategy(object):
    
    def __init__(self, worldWidth, explosion):
        self.worldWidth, self.explosion = worldWidth, explosion
        
    def moveCar(self, car, dx):
        newCarX = car.getX() + dx
        
        if newCarX < 0:
            newCarX = 0
        elif newCarX + car.getWidth() > self.worldWidth:
            newCarX = self.worldWidth - car.getWidth()
        
        newdx = newCarX - car.getX()
        car.setX(newCarX)
        self.explosion.move(newdx)
