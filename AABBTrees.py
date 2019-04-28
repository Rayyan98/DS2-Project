from aabbtree import AABB
from aabbtree import AABBTree
from MyRectangle import MyRectangle
from Collision_detection import Collision_Detection


class Collision_detection_AABB(Collision_Detection):
	def CheckCollisions(self , rects):
		self.tree = AABBTree()
		d = {i:rects[i] for i in range(len(rects))}
		j = 0
		for i in rects:
			aabb = AABB([(i.x, i.x+i.w),(i.y, i.y+i.h)])
			self.tree.add(aabb, j)
			j += 1
		
		s = set()
		for i in rects:
			a = self.tree.overlap_values(AABB([(i.x, i.x+i.w), (i.y, i.y+i.h)]))
			s = s.union({frozenset([i,d[j]]) for j in a if i != d[j]})
		return s
		
