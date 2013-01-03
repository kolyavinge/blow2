class World(object):
    
    def __init__(self, width, height, box2dWorld, car, enemies, explosion):
        self.width = width
        self.height = height
        self.box2dWorld = box2dWorld
        self.car = car
        self.enemies = enemies
        self.explosion = explosion

    def update(self):
        self.box2dWorld.Step(1.0 / 60.0, 1, 1)

    def isCompleted(self):
        return self.car.isBlowed() and self.car.isSleeping() and self.getDestroyedEnemiesCount() == 0

    def getDestroyedEnemiesCount(self):
        count = 0
        for enemy in self.enemies:
            if enemy.isDestroyed():
                count += 1
                
        return count

    def getCar(self):
        return self.car
    
    def getEnemies(self):
        return self.enemies
    
    def getEnemiesCount(self):
        return len(self.enemies)
        
    def getExplosion(self):
        return self.explosion

    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
