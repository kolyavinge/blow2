# -*- coding: utf-8 -*-

from blow.input.JoystickState import *

class InputManager(object):
    
    def __init__(self, controller, joy):
        self.controller = controller
        self.joy = joy
    
    def pollInputDevices(self):
        state = self.joy.getState()
        # car move
        if state.isPressed(JoystickButton_Left) or state.isHolded(JoystickButton_Left):
            self.controller.moveCar(-0.2)
        elif state.isPressed(JoystickButton_Right) or state.isHolded(JoystickButton_Right):
            self.controller.moveCar(0.2)
        # explosion move
        elif state.isPressed(JoystickButton_Up) or state.isHolded(JoystickButton_Up):
            self.controller.moveExplosion(0.1)
        elif state.isPressed(JoystickButton_Down) or state.isHolded(JoystickButton_Down):
            self.controller.moveExplosion(-0.1)
        # switch explosion volume
        elif state.isPressed(JoystickButton_5):
            self.controller.nextExplosionVolume()
        elif state.isPressed(JoystickButton_4):
            self.controller.prevExplosionVolume()
        # blow
        elif state.isPressed(JoystickButton_0):
            self.controller.blow()
        # next world
        elif state.isPressed(JoystickButton_3):
            self.controller.nextWorld()
        # reset world
        elif state.isPressed(JoystickButton_7):
            self.controller.resetWorld()
