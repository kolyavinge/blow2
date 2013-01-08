JoystickButton_Up = 1
JoystickButton_Down = 2
JoystickButton_Left = 3
JoystickButton_Right = 4
JoystickButton_0 = 5
JoystickButton_1 = 6
JoystickButton_2 = 7
JoystickButton_3 = 8
JoystickButton_4 = 9
JoystickButton_5 = 10
JoystickButton_6 = 11
JoystickButton_7 = 12

class JoystickError(RuntimeError):
    pass

class JoystickState(object):
    
    def __init__(self):
        self.pressed = []
        self.holded = []
        
    def press(self, button):
        if self.isHolded(button):
            raise JoystickError("button {0} is holded".format(button))
        if not button in self.pressed:
            self.pressed.append(button)
        
    def hold(self, button):
        if not self.isPressed(button):
            raise JoystickError("button {0} is not pressed".format(button))
        self.pressed.remove(button)
        self.holded.append(button)
        
    def setPressedAsHolded(self):
        self.holded.extend(self.pressed)
        self.pressed = []
        
    def release(self, button):
        try: self.pressed.remove(button)
        except: pass
        try: self.holded.remove(button)
        except: pass
        
    def getPressed(self):
        return self.pressed[:]
    
    def getHolded(self):
        return self.holded[:]
    
    def isPressed(self, button):
        return button in self.pressed
    
    def isHolded(self, button):
        return button in self.holded
    
    def isReleased(self, button):
        return not self.isPressed(button) and not self.isHolded(button)

    def getButtonString(self, button):
        if   button == JoystickButton_0:     return "0"
        elif button == JoystickButton_1:     return "1"
        elif button == JoystickButton_2:     return "2"
        elif button == JoystickButton_3:     return "3"
        elif button == JoystickButton_4:     return "4"
        elif button == JoystickButton_5:     return "5"
        elif button == JoystickButton_6:     return "6"
        elif button == JoystickButton_7:     return "7"
        elif button == JoystickButton_Up:    return "up"
        elif button == JoystickButton_Down:  return "down"
        elif button == JoystickButton_Left:  return "left"
        elif button == JoystickButton_Right: return "right"
    
    def __str__(self):
        result = 'pressed: '
        for button in self.pressed:
            result += self.getButtonString(button) + ' '
        result += '\nholded: '
        for button in self.holded:
            result += self.getButtonString(button) + ' '
        result += '\n'
        
        return result
