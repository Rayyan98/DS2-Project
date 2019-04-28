# Class for collision detection using array

from Collision_detection import Collision_Detection

class Collision_detection_Array(Collision_Detection):
	def CheckCollisions(self, rects):
		collision = set()
		for i in range(len(rects)):
			for j in range(i + 1, len(rects)):
				if self.takra(rects[i], rects[j]):
					collision.add(frozenset([i,j]))
		return collision
		
