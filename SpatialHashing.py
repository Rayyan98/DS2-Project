from Collision_detection import Collision_Detection
from MyScreen import MyScreen 

class Collision_Detection_Spatial_hashing(Collision_Detection):
    def __init__(self):
        self.Xboxes = MyScreen.width//100
        self.Yboxes = MyScreen.height//100

    def Hash(self, x,y):
        X = x//100
        Y = y//100

        h = X + Y * self.Xboxes
        return h
        
        
    def BroadPhase(self,rects):
        self.lst = [set() for i in range(self.Xboxes * self.Yboxes)]
        for r in rects:
            self.lst[self.Hash(r.x, r.y)].add(r)
            try:
                self.lst[self.Hash(r.x + r.w, r.y)].add(r)
            except:
                self.lst[self.Hash(r.x + r.w - 1, r.y)].add(r)
            try:
                self.lst[self.Hash(r.x, r.y + r.h)].add(r)
            except:
                self.lst[self.Hash(r.x, r.y + r.h - 1)].add(r)
            try:
                self.lst[self.Hash(r.x + r.w, r.y + r.h)].add(r)
            except:
                try:
                    self.lst[self.Hash(r.x + r.w - 1, r.y + r.h)].add(r)
                except:
                    try:
                        self.lst[self.Hash(r.x + r.w , r.y + r.h - 1)].add(r)
                    except:
                        self.lst[self.Hash(r.x + r.w - 1, r.y + r.h - 1)].add(r)


    def CheckCollisions(self, rects):
        self.BroadPhase(rects)
        S = set()
        for i in self.lst:
            while len(i) != 0:
                p = i.pop()
                for j in i:
                    if self.takra(p,j) == True:
                        S.add(frozenset([p,j]))
        return S




                        
        

        
