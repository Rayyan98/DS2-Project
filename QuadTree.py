from  Collision_detection import Collision_Detection
from MyScreen import MyScreen
from MyRectangle import MyRectangle
from MyRectangle import MyRectangle
import math

class Node(Collision_Detection):
    def __init__(self, rect):
        self.rect = rect
        self.rects = set()
        self.tl = None
        self.tr = None
        self.bl = None
        self.br = None
        self.children = []

    def insert(self, rect):
        if self.rect.w <= 50 or self.rect.h <= 50:
            self.rects.add(rect)
        else:
            self.rects.add(rect)
            if len(self.rects) > 4:
                if self.tl == None:
                    xmid = self.rect.w // 2 + self.rect.x
                    ymid = self.rect.h // 2 + self.rect.y
                    self.tl = Node(MyRectangle(self.rect.x, self.rect.y, self.rect.w // 2, self.rect.h //2))
                    self.tr = Node(MyRectangle(xmid, self.rect.y, math.ceil(self.rect.w / 2), self.rect.h // 2))
                    self.bl = Node(MyRectangle(self.rect.x, ymid, self.rect.w // 2, math.ceil(self.rect.h / 2)))
                    self.br = Node(MyRectangle(xmid, ymid, math.ceil(self.rect.w / 2), math.ceil(self.rect.h / 2)))
                    self.children = [self.tl, self.tr, self.bl, self.br]
                else:
                    r = [i for i in self.rects]
                    for j in r:
                        count = 0
                        for i in self.children:
                            if self.takra(j, i.rect):
                                u = i
                                count += 1
                                if count > 1:
                                    break
                        if(count == 1):
                            u.insert(j)
                            self.rects.remove(j)
            

    def CheckCollision(self, rects = []):
        s = set()
        r = [i for i in self.rects]
        for i in range(len(r) - 1):
            for j in range(i + 1, len(r)):
                if self.takra(r[i],r[j]):
                    s.add(frozenset([r[i],r[j]]))
        for i in rects:
            for j in self.rects:
                if self.takra(i,j):
                    s.add(frozenset([i,j]))
        for i in self.rects:
            rects.append(i)
        if self.tl != None:
            for i in self.children:
                s = s.union(i.CheckCollision(rects.copy()))
        return s

        
        
class Collision_Detection_Quad_Tree:
    def __init__(self):
        pass

    def CheckCollisions(self, rects):
        self.root = Node(MyRectangle(0,0,MyScreen.width, MyScreen.height))
        for i in rects:
            self.root.insert(i)
        return self.root.CheckCollision([])
        
    
