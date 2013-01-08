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
    
    def __del__(self):
        self.release()
    
    def release(self):
        os.close(self.jfd)
    
    def readAction(self):
        try:
            self.action = os.read(self.jfd, 8)
            return True
        except(OSError):
            return False
    
    def getState(self):
        self.joyState.setPressedAsHolded()
        while self.readAction():
            # button
            if self.isButton():
                if self.isPressed():
                    self.joyState.press(self.getButton())
                else:
                    self.joyState.release(self.getButton())
            # axis x
            elif self.isAxisX():
                if self.isRight():
                    self.joyState.press(JoystickButton_Right)
                elif self.isLeft():
                    self.joyState.press(JoystickButton_Left)
                else:
                    self.joyState.release(JoystickButton_Right)
                    self.joyState.release(JoystickButton_Left)
            # axis y
            elif self.isAxisY():
                if self.isDown():
                    self.joyState.press(JoystickButton_Down)
                elif self.isUp():
                    self.joyState.press(JoystickButton_Up)
                else:
                    self.joyState.release(JoystickButton_Down)
                    self.joyState.release(JoystickButton_Up)

        return self.joyState

    def isButton(self):
        return self.getActionByte(6) == 1
    
    def isPressed(self):
        return self.getActionByte(4) == 1
    
    def getButton(self):
        button = self.getActionByte(7)
        if   button == 0: return JoystickButton_0
        elif button == 1: return JoystickButton_1
        elif button == 2: return JoystickButton_2
        elif button == 3: return JoystickButton_3
        elif button == 4: return JoystickButton_4
        elif button == 5: return JoystickButton_5
        elif button == 6: return JoystickButton_6
        elif button == 7: return JoystickButton_7
    
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


# m = UnixJoystick(100) # raise error

#m = UnixJoystick()
#raw_input()
#print m.getState()
#raw_input()
#print m.getState()
#raw_input()
#print m.getState()
