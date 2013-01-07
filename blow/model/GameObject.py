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
    
    def getPosition(self):
        return (self.getX(), self.getY())
    
    def getCenterPosition(self):
        return (self.getCenterX(), self.getCenterY())
    
    def getCenterX(self):
        return self.getX() + self.getWidth() / 2.0
    
    def getCenterY(self):
        return self.getY() + self.getHeight() / 2.0
    
    def getWidth(self):
        return self.width
    
    def getHeight(self):
        return self.height
