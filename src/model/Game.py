from model.WorldBuilderUtils import buildWorldFromList
from model.Worlds import worldsList

GameState_Continue = 1
GameState_AllLevelsCompleted = 2

class Game(object):
    
    def __init__(self, worldsList):
        self.worldsList = worldsList
        self.state = GameState_Continue
        self.currentWorldIndex = 0
        self.__setCurrentWorld()
    
    def getWorld(self):
        return self.world
    
    def getState(self):
        return self.state
    
    def resetWorld(self):
        self.__setCurrentWorld()
        
    def nextWorld(self):
        if not self.world.isCompleted():
            raise GameError('current world is not completed')
        
        if self.hasNextWorld():
            self.currentWorldIndex += 1
            self.__setCurrentWorld()
        else:    
            self.state = GameState_AllLevelsCompleted
    
    def __setCurrentWorld(self):
        self.world = buildWorldFromList(self.worldsList[self.currentWorldIndex])
        
    def hasNextWorld(self):
        return self.currentWorldIndex + 1 < len(self.worldsList)


class GameError(RuntimeError):
    pass


def createGame():
    return Game(worldsList)


