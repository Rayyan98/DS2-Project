from Collision_detection import Collision_Detection
import random

class Node:
    def __init__(self, data = None , height = 0):
        self.data, self.next = data, [None for i in range(height + 1)]
    
class Collision_Detection_SkipList(Collision_Detection):
    def __init__(self):
        self.sentinel, self.h, self.size = Node(), 0, 0

    def pick_height(self):
        k = 0
        while random.randint(0,1):
            k+=1
        return k
    
    def Add(self, rect):
        u, r, s = self.sentinel, self.h, [None for i in range(self.h + 1)]
        while r >= 0:
            while u.next[r] != None and u.next[r].data.x < rect.x:
                u = u.next[r]
            s[r] = u
            r = r - 1
        p = self.pick_height()
        w = Node(rect, p)
        while self.h < p:
            self.h+=1
            s.append(self.sentinel)
            self.sentinel.next.append(None)
        for i in range(len(w.next)):
            w.next[i], s[i].next[i] = s[i].next[i], w
        self.size += 1
        return True
    
    def CheckCollisions(self, rects):
        self.__init__()
        for i in rects:
            self.Add(i)
        S = set()
        if self.size > 1:
            i, j = self.sentinel.next[0], self.sentinel.next[0].next[0]
            while i.next[0] != None:
                while j != None:
                    if i.data.x  + i.data.w < j.data.x:
                        break
                    else:                        
                        if self.takra(i.data, j.data):
                            S.add(frozenset([i.data,j.data]))
                    j = j.next[0]
                j = i.next[0].next[0]
                i = i.next[0]
                
        return S
                
