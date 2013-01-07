# -*- coding: utf-8 -*-

class InputManager(object):
    
    def __init__(self, controller, joy):
        self.controller = controller
        self.joy = joy
    
    def pollInputDevices(self):
        state = self.joy.getState()
        # car move
        if state.isLeftPressed():
            self.controller.moveCar(-0.2)
        elif state.isRightPressed():
            self.controller.moveCar(0.2)
        # explosion move
        elif state.isUpPressed():
            self.controller.moveExplosion(0.1)
        elif state.isDownPressed():
            self.controller.moveExplosion(-0.1)
        # switch explosion volume
        if state.isButtonPressed(5):
            self.controller.nextExplosionVolume()
        elif state.isButtonPressed(4):
            self.controller.prevExplosionVolume()
        # blow
        elif state.isButtonPressed(0):
            self.controller.blow()
        # next world
        elif state.isButtonPressed(3):
            self.controller.nextWorld()
        # reset world
        elif state.isButtonPressed(7):
            self.controller.resetWorld()
