# Bigger imports
import pygame
import random

# Smaller imports
from MyRectangle import MyRectangle
from MyColor import MyColor
from MyScreen import MyScreen

# Algorithm imports
from Collision_detection_Array import Collision_detection_Array

FPS = 20


pygame.init()


MyScreen.width = 1000
MyScreen.height = 600

r = []
for i in range(2):
	l= random.randint(10,50)
	vx = random.randint(3, 10)
	vy = random.randint(3, 10)
	r.append(MyRectangle(random.randint(0, MyScreen.width - 60), random.randint(0, MyScreen.height - 60), l, l, 0 , 0))


screen = pygame.display.set_mode((MyScreen.width, MyScreen.height))
clock = pygame.time.Clock()

arrayDetection = Collision_detection_Array()

loop = True

while loop:
	a = pygame.time.get_ticks()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				r[1].vy += -1
			if event.key == pygame.K_DOWN:
				r[1].vy += 1
			if event.key == pygame.K_LEFT:
				r[1].vx += -1
			if event.key == pygame.K_RIGHT:
				r[1].vx += 1
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_UP:
				r[1].vy += 1
			if event.key == pygame.K_DOWN:
				r[1].vy += -1
			if event.key == pygame.K_LEFT:
				r[1].vx += 1
			if event.key == pygame.K_RIGHT:
				r[1].vx += -1	
				


	for i in r:
		i.Move()
	
	print(arrayDetection.CheckCollisions(r))

	screen.fill((MyColor.black))
	
	for i in r:
		pygame.draw.rect(screen, (255,255,255), i.GetBounds(), 0)

	pygame.display.flip()
	
	clock.tick(FPS)
	b = pygame.time.get_ticks()
	if a-b > 1.5/FPS:
		print(a-b)
	
pygame.quit()

