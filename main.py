# Bigger imports
import pygame

# Smaller imports
from MyRectangle import MyRectangle
from MyColor import MyColor

pygame.init()

screen = pygame.display.set_mode((1000,600))
clock = pygame.time.Clock()

r = MyRectangle(0,0,50,50,1,1)
loop = True

while loop:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
	
	r.Move()


	screen.fill((MyColor.black))
	pygame.draw.rect(screen, (255,255,255), r.GetBounds(), 0)

	pygame.display.flip()
	
	clock.tick(30)
	
