from model.WorldBuilder import *

def buildWorldFromList(worldList):
    __validateWorldList(worldList)
    
    builder = WorldBuilder()
    
    worldSizeTuple = worldList[0]
    worldWidth = worldSizeTuple[0]
    worldHeight = worldSizeTuple[1]
    builder.setSize(worldWidth, worldHeight)
    
    enemiesTuples = worldList[1]
    for enemy in enemiesTuples:
        x = enemy[0]
        y = enemy[1]
        width = enemy[2]
        height = enemy[3]
        builder.addEnemy(x, y, width, height)
    
    return builder.buildWorld()

def __validateWorldList(worldList):
    if len(worldList) != 2:
        raise ValueError('worldList length must be 2')
    
    worldSizeTuple = worldList[0]
    if len(worldSizeTuple) != 2:
        raise ValueError('worldSizeTuple length must be 2')
    
    enemies = worldList[1]
    for enemy in enemies:
        if len(enemy) != 4:
            raise ValueError('enemyTuple length must be 2')
    
