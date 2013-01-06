from blow.model.Car import Car
from blow.model.Enemy import Enemy
from lib.box2d.Box2D import b2ContactListener

class EnemyContactListener(b2ContactListener):

    def Add(self, point):
        obj1 = point.shape1.GetBody().GetUserData()
        obj2 = point.shape2.GetBody().GetUserData()
        if (type(obj1) is Car and type(obj2) is Enemy):
            obj2.destroy()
        elif (type(obj2) is Car and type(obj1) is Enemy):
            obj1.destroy()
