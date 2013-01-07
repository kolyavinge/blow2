import os
from blow.input.JoystickState import *

class UnixJoystick(object):
    
    def __init__(self, joyNumber=0):
        try:
            jsFile = '/dev/input/js{0}'.format(joyNumber)
            self.jfd = os.open(jsFile, os.O_RDONLY | os.O_NONBLOCK)  # non-blocking read
            os.read(self.jfd, 1024)  # skip init state
            self.joyState = JoystickState()
        except(OSError):
            raise JoystickError('joystick "{0}" not found'.format(jsFile))
    
    def release(self):
        os.close(self.jfd)
    
    def readAction(self):
        try:
            self.action = os.read(self.jfd, 8)
            return True
        except(OSError):
            return False
    
    def getState(self):
        while self.readAction():
            # button
            if self.isButton():
                if self.isPressed():
                    self.joyState.pressButton(self.getButtonNumber())
                else:
                    self.joyState.releaseButton(self.getButtonNumber())
            # axis x
            elif self.isAxisX():
                if self.isRight():
                    self.joyState.pressRight()
                elif self.isLeft():
                    self.joyState.pressLeft()
                else:
                    self.joyState.releaseRight()
                    self.joyState.releaseLeft()
            # axis y
            elif self.isAxisY():
                if self.isDown():
                    self.joyState.pressDown()
                elif self.isUp():
                    self.joyState.pressUp()
                else:
                    self.joyState.releaseDown()
                    self.joyState.releaseUp()

        return self.joyState

    def isButton(self):
        return self.getActionByte(6) == 1
    
    def isPressed(self):
        return self.getActionByte(4) == 1
    
    def getButtonNumber(self):
        return self.getActionByte(7)
    
    def isAxisX(self):
        return self.getActionByte(7) == 0
    
    def isRight(self):
        return self.getActionByte(4) == 255
    
    def isLeft(self):
        return self.getActionByte(4) == 1
    
    def isAxisY(self):
        return self.getActionByte(7) == 1
    
    def isDown(self):
        return self.getActionByte(4) == 255
    
    def isUp(self):
        return self.getActionByte(4) == 1

    def getActionByte(self, byte):
        return ord(self.action[byte])


#m = UnixJoystick(100) # raise error

#m = UnixJoystick()
#raw_input()
#print m.getState()

