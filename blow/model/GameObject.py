class GameObject(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getCenterX(self):
        return self.x + self.width / 2.0
    
    def getCenterY(self):
        return self.y + self.height / 2.0
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
