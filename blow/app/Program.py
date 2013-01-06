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
from pyglet import image
from pyglet.window import Window

windowWidth = 1024
windowHeight = 768
resourcePath = '/home/kolya/Исходники/EclipseProjects/blow2/res/'
backgroundImagePath = resourcePath + 'background.jpg'
wallImagePath = resourcePath + 'wall.png'
carImagePath = resourcePath + 'car.png'
enemyImagePath = resourcePath + 'enemy.png'
explosionImagePath = resourcePath + 'explosion.png'
updateWorldInerval = 0.1

class Program(object):
    
    def updateWorld(self, dt):
        self.inputManager.pollInputDevices()
        self.game.getWorld().update()
        
    def drawScene(self):
        self.window.clear()
        self.worldView.draw()
    
    def run(self):
        self.game = createGame()
        
        qx = windowWidth / self.game.getWorld().getWidth()
        qy = windowHeight / self.game.getWorld().getHeight()
        q = qx if qx < qy else qy
        offsetX = (windowWidth - q * self.game.getWorld().getWidth()) / 2.0
        
        childWorldViews = []
        
        explosionImage = pyglet.image.load(explosionImagePath)
        explosionSprite = pyglet.sprite.Sprite(explosionImage)
        explosionView = ExplosionView(self.game.getWorld().getExplosion(), offsetX, q, explosionSprite)
        childWorldViews.append(explosionView)
        
        carImage = pyglet.image.load(carImagePath)
        carSprite = pyglet.sprite.Sprite(carImage)
        carView = CarView(self.game.getWorld().getCar(), offsetX, q, carSprite)
        childWorldViews.append(carView)
        
        enemyImage = pyglet.image.load(enemyImagePath)
        for enemy in self.game.getWorld().getEnemies():
            enemySprite = pyglet.sprite.Sprite(enemyImage)
            enemyView = EnemyView(enemy, offsetX, q, enemySprite)
            childWorldViews.append(enemyView)
        
        backgroundImage = image.load(backgroundImagePath)
        wallImage = image.load(wallImagePath)
        self.worldView = WorldView(self.game.getWorld(), offsetX, q, backgroundImage, wallImage, childWorldViews)
        
        gameController = GameController(self.game, self.worldView)
        
        joy = UnixJoystick()
        self.inputManager = InputManager(gameController, joy)
        
        self.window = Window(windowWidth, windowHeight)
        self.window.on_draw = self.drawScene

        pyglet.clock.schedule_interval(self.updateWorld, updateWorldInerval)
        pyglet.app.run()


# запуск главного окна
program = Program()
program.run()

