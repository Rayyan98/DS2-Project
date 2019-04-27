# Creating Rectangle Class

class Rectangle:
	def __init__(self, x, y, w, h):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		
	def GetBounds(self):
		return (self.x, self.y, self.w, self.h)

