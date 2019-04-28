# Bigger imports
import pygame
import random


# Smaller imports
from MyRectangle import MyRectangle
from MyColor import MyColor
from MyScreen import MyScreen
from stopwatch import Stopwatch


# Algorithm imports
from Collision_detection_Array import Collision_detection_Array


FPS = 20
MyScreen.width = 900
MyScreen.height = 600


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


r = []
for i in range(100):
	l= random.randint(10,40)
	vx = random.randint(3, 10)
	vy = random.randint(3, 10)
	r.append(MyRectangle(random.randint(0, MyScreen.width - 40), random.randint(0, MyScreen.height - 40), l, l, vx , vy))


screen = pygame.display.set_mode((int(MyScreen.width * 1.4), MyScreen.height))
clock = pygame.time.Clock()


arrayDetection = Collision_detection_Array()
arrayStop = Stopwatch()
arrayLabel = myfont.render("Array based", False, MyColor.white)

loop = True


while loop:
	a = pygame.time.get_ticks()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			loop = False
		# elif event.type == pygame.KEYDOWN:
			# if event.key == pygame.K_UP:
				# r[1].vy += -1
			# if event.key == pygame.K_DOWN:
				# r[1].vy += 1
			# if event.key == pygame.K_LEFT:
				# r[1].vx += -1
			# if event.key == pygame.K_RIGHT:
				# r[1].vx += 1
		# elif event.type == pygame.KEYUP:
			# if event.key == pygame.K_UP:
				# r[1].vy += 1
			# if event.key == pygame.K_DOWN:
				# r[1].vy += -1
			# if event.key == pygame.K_LEFT:
				# r[1].vx += 1
			# if event.key == pygame.K_RIGHT:
				# r[1].vx += -1	
				
	for i in r:
		i.Move()
	
	arrayStop.start()
	arrayResult = arrayDetection.CheckCollisions(r)
	arrayStop.stop()
	arrayTime = myfont.render(str(arrayStop.time_elapsed())  + ' ms', False, MyColor.white)
	arrayStop.reset()

	screen.fill((MyColor.black))
	
	for i in r:
		pygame.draw.rect(screen, (255,255,255), i.GetBounds(), 0)

	screen.blit(arrayLabel,(MyScreen.width * 1.05, 0))
	screen.blit(arrayTime,(MyScreen.width * 1.05, 30))

	pygame.display.flip()
	
	clock.tick(FPS)

	b = pygame.time.get_ticks()

	if a-b > 1.5/FPS:
		print(a-b)
	
pygame.quit()

