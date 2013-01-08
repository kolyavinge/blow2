# -*- coding: utf-8 -*-

from lib.box2d.Box2D import *
from blow.model.Car import *
from blow.model.CarMovingStrategy import *
from blow.model.Enemy import *
from blow.model.EnemyContactListener import *
from blow.model.Explosion import *
from blow.model.ExplosionMovingStrategy import *
from blow.model.World import *

class WorldBuilder(object):
    
    def __init__(self):
        self.enemies = []
    
    def buildWorld(self):
        box2dWorld = self.createBox2dWorld()
        self.createGroundAndWalls(box2dWorld)
        explosion = self.createExplosion()
        car = self.createCar(box2dWorld)
        self.bindCarAndExplosion(explosion, car)
        self.createEnemies(box2dWorld)
        self.createEnemyContactListener(box2dWorld)
        
        return World(self.worldWidth, self.worldHeight, box2dWorld, car, self.enemies, explosion)
    
    def createBox2dWorld(self):
        enviroment = b2AABB()
        enviroment.lowerBound = (-10.0, -10.0)
        enviroment.upperBound = (self.worldWidth + 10.0, 100.0 * self.worldHeight)
        gravity = (0.0, -50.0)
        doSleep = True
        
        return b2World(enviroment, gravity, doSleep)
    
    def createGroundAndWalls(self, box2dWorld):
        bodyDef = b2BodyDef()
        shape = b2PolygonDef()
        
        # ground
        bodyDef.position = (self.worldWidth / 2.0, -1.0)
        shape.SetAsBox(self.worldWidth / 2.0, 1.0)
        box2dWorld.CreateBody(bodyDef).CreateShape(shape)
        
        # left wall
        bodyDef.position = (-1.0, self.worldHeight / 2.0)
        shape.SetAsBox(1.0, self.worldHeight)
        box2dWorld.CreateBody(bodyDef).CreateShape(shape)
        
        # right wall
        bodyDef.position = (self.worldWidth + 1.0, self.worldHeight / 2.0)
        shape.SetAsBox(1.0, self.worldHeight)
        box2dWorld.CreateBody(bodyDef).CreateShape(shape)
    
    def createExplosion(self):
        return Explosion(self.worldWidth / 2.0)
    
    def createCar(self, box2dWorld):
        bodyDef = b2BodyDef()
        bodyDef.position = (self.worldWidth / 2.0, carHeight / 2.0)
        box2dCarBody = box2dWorld.CreateBody(bodyDef)
        shape = b2PolygonDef()
        shape.SetAsBox(carWidth / 2.0, carHeight / 2.0)
        shape.density = 1.0
        box2dCarBody.CreateShape(shape)
        box2dCarBody.SetMassFromShapes()
        car = Car(box2dCarBody)
        box2dCarBody.SetUserData(car)
        
        return car
    
    def bindCarAndExplosion(self, explosion, car):
        car.setMovingStrategy(CarMovingStrategy(self.worldWidth, explosion))
        explosion.setBlowingObject(car)
        explosion.setMovingStrategy(ExplosionMovingStrategy(car))
    
    def createEnemies(self, box2dWorld):
        for enemy in self.enemies:
            self.createEnemyBody(box2dWorld, enemy)
    
    def createEnemyBody(self, box2dWorld, enemy):
        bodyDef = b2BodyDef()
        bodyDef.position = (enemy.getCenterX(), enemy.getCenterY())
        anchor = box2dWorld.CreateBody(bodyDef)
        
        enemyBody = box2dWorld.CreateBody(bodyDef)
        shape = b2PolygonDef()
        shape.SetAsBox(enemy.getWidth() / 2.0, enemy.getHeight() / 2.0)
        shape.density = 0.001
        enemyBody.CreateShape(shape)
        enemyBody.SetMassFromShapes()
        enemyBody.SetUserData(enemy)
        
        joint = b2RevoluteJointDef()
        joint.body1 = anchor
        joint.body2 = enemyBody
        joint.lowerAngle = 0
        joint.upperAngle = 0
        joint.collideConnected = False
        box2dWorld.CreateJoint(joint)
    
    def createEnemyContactListener(self, box2dWorld):
        # для того чтобы enemyContactListener раньше времени не затерся сборщиком мусора
        # помещаем его в объект box2dWorld
        box2dWorld.enemyContactListener = EnemyContactListener()
        box2dWorld.SetContactListener(box2dWorld.enemyContactListener)
        
    def setSize(self, width, height):
        self.worldWidth = width
        self.worldHeight = height
        
    def addEnemy(self, x, y, width, height):
        if self.inWorld(x, y, width, height):
            enemy = Enemy(x, y, width, height)
            self.enemies.append(enemy)
        else:
            raise WorldError('enemy not in world {0}:{1}'.format(x, y))

    def inWorld(self, x, y, width, height):
        return (x >= 0) and (y >= 0) and (x + width <= self.worldWidth) and (y + height <= self.worldHeight)


