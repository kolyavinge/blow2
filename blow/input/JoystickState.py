class JoystickState(object):
    
    def __init__(self):
        self.up = self.down = self.left = self.right = False
        self.buttons = []
    
    def __str__(self):
        return "left={0}, right={1}, up={2}, down={3}, buttons={4}".format(self.left, self.right, self.up, self.down, self.buttons)
        
    def isLeftPressed(self):
        return self.left
    
    def isRightPressed(self):
        return self.right
    
    def isUpPressed(self):
        return self.up
    
    def isDownPressed(self):
        return self.down    
        
    def getPressedButtons(self):
        return self.buttons
    
    def pressLeft(self):
        self.left = True
        
    def releaseLeft(self):
        self.left = False
        
    def pressRight(self):
        self.right = True
        
    def releaseRight(self):
        self.right = False
        
    def pressUp(self):
        self.up = True
        
    def releaseUp(self):
        self.up = False
    
    def pressDown(self):
        self.down = True
        
    def releaseDown(self):
        self.down = False

    def pressButton(self, button):
        if not button in self.buttons:
            self.buttons.append(button)
    
    def releaseButton(self, button):
        if button in self.buttons:
            self.buttons.remove(button)
        
    def isButtonPressed(self, button):
        return button in self.buttons
    

class JoystickError(RuntimeError):
    pass

