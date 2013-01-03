from Box2D import *
from model.Car import *
from model.CarMovingStrategy import *
from model.Enemy import *
from model.Explosion import *
from model.ExplosionMovingStrategy import *
from model.World import *

class WorldBuilder(object):
    
    def __init__(self):
        self.enemies = []
    
    def buildWorld(self):
        enviroment = b2AABB()
        enviroment.lowerBound = (-10.0, -10.0)
        enviroment.upperBound = (self.worldWidth + 10.0, 2.0 * self.worldHeight)
        gravity = (0.0, -1.0)
        doSleep = True
        box2dWorld = b2World(enviroment, gravity, doSleep)
        
        bodyDef = b2BodyDef()
        shape = b2PolygonDef()
        
        # bottom
        bodyDef.position = (self.worldWidth / 2.0, -1.0)
        shape.SetAsBox(self.worldWidth / 2.0, 1.0)
        box2dWorld.CreateBody(bodyDef).CreateShape(shape)
        
        # left
        bodyDef.position = (-1.0, self.worldHeight / 2.0)
        shape.SetAsBox(1.0, self.worldHeight)
        box2dWorld.CreateBody(bodyDef).CreateShape(shape)
        
        # right
        bodyDef.position = (self.worldWidth + 1.0, self.worldHeight / 2.0)
        shape.SetAsBox(1.0, self.worldHeight)
        box2dWorld.CreateBody(bodyDef).CreateShape(shape)
        
        explosion = Explosion(self.worldWidth / 2.0)
        
        bodyDef = b2BodyDef()
        bodyDef.position = (self.worldWidth / 2.0, carHeight / 2.0)
        box2dCarBody = box2dWorld.CreateBody(bodyDef)
        shape = b2PolygonDef()
        shape.SetAsBox(carWidth / 2.0, carHeight / 2.0)
        shape.density = 1.0
        box2dCarBody.CreateShape(shape)
        box2dCarBody.SetMassFromShapes()
        
        ms = CarMovingStrategy(self.worldWidth, explosion)
        
        car = Car(box2dCarBody, ms)
        
        explosion.setBlowingObject(car)
        explosion.setMovingStrategy(ExplosionMovingStrategy(car))
        
        world = World(self.worldWidth, self.worldHeight, box2dWorld, car, self.enemies, explosion)
        
        return world
        
    def setSize(self, width, height):
        self.worldWidth = width
        self.worldHeight = height
        
    def addEnemy(self, x, y, width, height):
        enemy = Enemy(x, y, width, height)
        self.enemies.append(enemy)
