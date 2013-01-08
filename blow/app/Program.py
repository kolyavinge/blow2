# -*- coding: utf-8 -*-

from blow.model.Game import *
from blow.view.CarView import *
from blow.view.EnemyView import *
from blow.view.ExplosionView import *
from blow.view.WorldView import *
from blow.input.UnixJoystick import *
from blow.input.GameController import *
from blow.input.InputManager import *
import pyglet

windowWidth = 1024
windowHeight = 768
resourcePath = '/home/kolya/Исходники/EclipseProjects/blow2/res/'
backgroundImagePath = resourcePath + 'background.jpg'
wallImagePath = resourcePath + 'wall.png'
carImagePath = resourcePath + 'car.png'
enemyImagePath = resourcePath + 'enemy.png'
explosionImagePath = resourcePath + 'explosion.png'
updateWorldInerval = 0.01

class Program(object):
    
    def updateWorld(self, dt):
        self.inputManager.pollInputDevices()
        self.game.getWorld().update()
        
    def drawScene(self):
        self.window.clear()
        self.worldView.draw()
    
    def getSizeFactor(self, world):
        qx = windowWidth / world.getWidth()
        qy = windowHeight / world.getHeight()
        return qx if qx < qy else qy
    
    def getOffsetX(self, world, sizeFactor):
        return (windowWidth - sizeFactor * world.getWidth()) / 2.0
    
    def changeWorld(self, world):
        sizeFactor = self.getSizeFactor(world)
        offsetX = self.getOffsetX(world, sizeFactor)
        
        childWorldViews = []
        
        explosionImage = pyglet.image.load(explosionImagePath)
        explosionSprite = pyglet.sprite.Sprite(explosionImage)
        explosionView = ExplosionView(world.getExplosion(), offsetX, sizeFactor, explosionSprite)
        childWorldViews.append(explosionView)
        
        carImage = pyglet.image.load(carImagePath)
        carSprite = pyglet.sprite.Sprite(carImage)
        carView = CarView(world.getCar(), offsetX, sizeFactor, carSprite)
        childWorldViews.append(carView)
        
        enemyImage = pyglet.image.load(enemyImagePath)
        for enemy in world.getEnemies():
            enemySprite = pyglet.sprite.Sprite(enemyImage)
            enemyView = EnemyView(enemy, offsetX, sizeFactor, enemySprite)
            childWorldViews.append(enemyView)
        
        backgroundImage = pyglet.image.load(backgroundImagePath)
        wallImage = pyglet.image.load(wallImagePath)
        self.worldView = WorldView(world, offsetX, sizeFactor, backgroundImage, wallImage, childWorldViews)
        
        gameController = GameController(self.game)
        
        joy = UnixJoystick()
        self.inputManager = InputManager(gameController, joy)
        
    def run(self):
        self.game = createGame()
        self.game.onChangeWorld = self.changeWorld
        self.changeWorld(self.game.getWorld())
        self.window = pyglet.window.Window(windowWidth, windowHeight)
        self.window.on_draw = self.drawScene
        pyglet.clock.schedule_interval(self.updateWorld, updateWorldInerval)
        pyglet.app.run()


# запуск главного окна
program = Program()
program.run()

