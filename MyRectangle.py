# Creating Rectangle Class

class MyRectangle:
	def __init__(self, x, y, w, h, vx= 0, vy = 0):
		self.x = x
		self.y = y
		self.w = w
		self.h = h
		self.vx = vx
		self.vy = vy
		
	def GetBounds(self):
		return (self.x, self.y, self.w, self.h)

	def Move(self):
		self.x += self.vx
		self.y += self.vy

