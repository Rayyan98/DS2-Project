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
        
    
    
##class Collision_Detection_Quad_Tree(Collision_Detection):
##    def __init__(self, rect):
##        self.rect = rect
##        self.topLeftTree = None
##        self.topRightTree = None
##        self.botLeftTree = None
##        self.botRightTree = None
##    def inBoundary(self, p):
##        return p[0] >= self.topLeft[0] and p[0] <= self.botRight[0] and p[1] >= self.topLeft[1] and p[1] <= self.botRight[1]
##    def insert(self, node):
##        if not self.inBoundary((node.pos[0], node.pos[1])):
##            return None
##        if abs(self.topLeft[0] - self.botRight[0]) <= 1 and abs(self.topLeft[1] - self.botRight[1]) <= 1:
##            if n == None:
##                n = node
##            return None
##        if (self.topLeft[0] + self.botRight[0]) / 2 >= node.pos[0]:
##            if (self.topLeft[1] + self.botRight[1]) / 2 >= node.pos[1]:
##                if self.topLeftTree == None:
##                    self.topLeftTree = Collision_Detection_Quad_Tree((self.topLeft[0], self.topLeft[1]), ((self.topLeft[0] + self.botRight[0]) / 2, (self.topLeft[1] + self.botRight[1]) / 2))
##                self.topLefttree.insert(node)
##            else:
##                if self.botLeftTree == None:
##                    self.botLeftTree = Collision_Detection_Quad_Tree((self.topLeft[0], (self.topLeft[1] + self.botRight[1]) / 2), ((self.topLeft[0] + self.botRight[0]) / 2, self.botRight[1]))
##                self.botLefttree.insert(node)
##        else:
##            if (self.topLeft[1] + self.botRight[1]) / 2 >= node.pos[1]:
##                if self.topRightTree == None:
##                    self.topRightTree = Collision_Detection_Quad_Tree(((self.topLeft[0] + self.botRight[0]) / 2, self.topLeft[1]), (self.botRight[0], (self.topLeft[1] + self.botRight[1]) / 2))
##                self.topRighttree.insert(node)
##            else:
##                if self.botRightTree == None:
##                    self.botRightTree = Collision_Detection_Quad_Tree(((self.topLeft[0] + self.botRight[0]) / 2, (self.topLeft[1] + botRight[1]) / 2), (self.botRight[0], self.botRight[1]))
##                self.botRighttree.insert(node)
##    def CheckCollisions(self, rects):
        
