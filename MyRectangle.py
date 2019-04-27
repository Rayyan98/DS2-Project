# Creating Rectangle Class

from MyScreen import MyScreen


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

		endx = self.x + self.w
		if self.x < 0:
			self.x = -self.x 
			self.vx = -self.vx
			self.vy += 1
		elif endx > MyScreen.width:
			self.vx = - self.vx
			endx = 2 * MyScreen.width - endx
			self.x = endx - self.w
			self.vy -= 1

		endy = self.y  + self.h
		if self.y < 0:
			self.y = -self.y
			self.vy = -self.vy
			self.vx += 1
		elif endy > MyScreen.height:
			self.vy = - self.vy
			endy = 2 * MyScreen.height - endy
			self.y = endy - self.h
			self.vx -= -1

