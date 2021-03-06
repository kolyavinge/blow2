from blow.model.WorldBuilderUtils import buildWorldFromList
from blow.model.Worlds import worldsList

GameState_Continue = 1
GameState_AllLevelsCompleted = 2

class Game(object):
    
    def __init__(self, worldsList):
        self.worldsList = worldsList
        self.state = GameState_Continue
        self.currentWorldIndex = 0
        self.__setCurrentWorld()
        self.onChangeWorld = None
    
    def getWorld(self):
        return self.world
    
    def getState(self):
        return self.state
    
    def resetWorld(self):
        self.__setCurrentWorld()
        self.__raiseOnChangeWorld()
        
    def nextWorld(self):
        if not self.world.isCompleted():
            raise GameError('current world is not completed')
        
        if self.hasNextWorld():
            self.currentWorldIndex += 1
            self.__setCurrentWorld()
            self.__raiseOnChangeWorld()
        else:
            self.state = GameState_AllLevelsCompleted
    
    def __setCurrentWorld(self):
        self.world = buildWorldFromList(self.worldsList[self.currentWorldIndex])
        
    def hasNextWorld(self):
        return self.currentWorldIndex + 1 < len(self.worldsList)

    def __raiseOnChangeWorld(self):
        if self.onChangeWorld != None:
            self.onChangeWorld(self.world)
    
class GameError(RuntimeError):
    pass


def createGame():
    return Game(worldsList)


