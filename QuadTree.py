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


	def insert(self, rect):
		if self.rect.w <= 100 or self.rect.h <= 100:
			self.rects.add(rect)
		else:
			self.rects.add(rect)
			if len(self.rects) > 7:
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
						if j.x + j.w < self.rect.x + self.rect.w // 2:
							if  j.y + j.h < self.rect.y + self.rect.h // 2:
								self.tl.insert(j)
								self.rects.remove(j)
							elif j.y >= math.ceil(self.rect.h / 2) + self.rect.y:
								self.bl.insert(j)
								self.rects.remove(j)
						elif j.x >= self.rect.x + math.ceil(self.rect.w / 2):
							if  j.y + j.h < self.rect.y + self.rect.h // 2:
								self.tr.insert(j)
								self.rects.remove(j)
							elif j.y >= math.ceil(self.rect.h / 2) + self.rect.y:
								self.br.insert(j)
								self.rects.remove(j)
							
                    # r = [i for i in self.rects]
                    # for j in r:
                        # count = 0
                        # for i in self.children:
                            # if self.takra(j, i.rect):
                                # u = i
                                # count += 1
                                # if count > 1:
                                    # break
                        # if(count == 1):
                            # u.insert(j)
                            # self.rects.remove(j)

	def AddRects(self,  rects):
		if self.rect.w <= 80 or self.rect.h <= 80 or len(rects) < 5:
			for i in rects:
				self.rects.add(i)
		else:
			if self.tl == None:
				xmid = self.rect.w // 2 + self.rect.x
				ymid = self.rect.h // 2 + self.rect.y
				self.tl = Node(MyRectangle(self.rect.x, self.rect.y, self.rect.w // 2, self.rect.h //2))
				self.tr = Node(MyRectangle(xmid, self.rect.y, math.ceil(self.rect.w / 2), self.rect.h // 2))
				self.bl = Node(MyRectangle(self.rect.x, ymid, self.rect.w // 2, math.ceil(self.rect.h / 2)))
				self.br = Node(MyRectangle(xmid, ymid, math.ceil(self.rect.w / 2), math.ceil(self.rect.h / 2)))
			tl = []
			bl = []
			tr = []
			br = []
			for j in rects:
				if j.x + j.w < self.rect.x + self.rect.w // 2:
					if  j.y + j.h < self.rect.y + self.rect.h // 2:
						tl.append(j)
					elif j.y >= math.ceil(self.rect.h / 2) + self.rect.y:
						bl.append(j)
					else:
						self.rects.add(j)
				elif j.x >= self.rect.x + math.ceil(self.rect.w / 2):
					if  j.y + j.h < self.rect.y + self.rect.h // 2:
						tr.append(j)
					elif j.y >= math.ceil(self.rect.h / 2) + self.rect.y:
						br.append(j)
					else:
						self.rects.add(j)
				else:
					self.rects.add(j)
			self.tl.AddRects(tl)
			self.bl.AddRects(bl)
			self.tr.AddRects(tr)
			self.br.AddRects(br)
            

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
		tlcopy = rects.copy()
		blcopy = rects.copy()
		trcopy = rects.copy()
		brcopy = rects.copy()
		for j in self.rects:
			if j.x + j.w < self.rect.x + self.rect.w // 2:
				if  j.y + j.h < self.rect.y + self.rect.h // 2:
					tlcopy.append(j)
				elif j.y >= math.ceil(self.rect.h / 2) + self.rect.y:
					blcopy.append(j)
				else:
					tlcopy.append(j)
					blcopy.append(j)
			elif j.x >= self.rect.x + math.ceil(self.rect.w / 2):
				if  j.y + j.h < self.rect.y + self.rect.h // 2:
					trcopy.append(j)
				elif j.y >= math.ceil(self.rect.h / 2) + self.rect.y:
					brcopy.append(j)
				else:
					trcopy.append(j)
					brcopy.append(j)
			else:
				if  j.y + j.h < self.rect.y + self.rect.h // 2:
					trcopy.append(j)
					tlcopy.append(j)
				elif j.y >= math.ceil(self.rect.h / 2) + self.rect.y:
					brcopy.append(j)
					blcopy.append(j)
				else:
					trcopy.append(j)
					brcopy.append(j)
					tlcopy.append(j)
					blcopy.append(j)
			
		if self.tl != None:
			s = s.union(self.tl.CheckCollision(tlcopy))
			s = s.union(self.bl.CheckCollision(blcopy))
			s = s.union(self.tr.CheckCollision(trcopy))
			s = s.union(self.br.CheckCollision(brcopy))
		return s

        
        
class Collision_Detection_Quad_Tree:
	def __init__(self):
		pass

	def CheckCollisions(self, rects):
		self.root = Node(MyRectangle(0,0,MyScreen.width, MyScreen.height))
		self.root.AddRects(rects)
		# for i in rects:
			# self.root.insert(i)
		return self.root.CheckCollision([])
        
    
