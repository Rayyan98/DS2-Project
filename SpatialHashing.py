from Collision_detection import Collision_Detection
from MyScreen import MyScreen 

class Collision_Detection_Spatial_hashing(collision_Detection):
    def __init__(rects):
        self.Xboxes = int(MyScreen.width/100)
        self.Yboxes = int(MyScreen.height/100)

    def Hash(x,y):
        X = x//100
        Y = y//100

        h = X + Y*self.Xboxes
        return h
        
        
    def BroadPhase(self,rects):
        self.lst = [set() for i in range(self.Xboxes * self.Yboxes)]
        for r in rects:
            self.lst[Hash(r.x,r.y)].add(r)
            self.lst[Hash(r.x + r.w,r.y)].add(r)
            self.lst[Hash(r.x,r.y + r.h)].add(r)
            self.lst[Hash(r.x + r.w,r.y + r.h)].add(r)


    def CheckCollisions(self, rects):
        self.BroadPhase(rects)
        S = set()
        for i in self.lst:
            while len(i) != 0:
                p = i.pop()
                for j in i:
                    if self.takra(p,j) == True:
                        S.add(frozenset([p,j])
        return S




                        
        

        
