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
from SpatialHashing import Collision_Detection_Spatial_hashing


def GetRandomRects(n):
	r = []
	for i in range(n):
		l= random.randint(10,40)
		vx = random.randint(3, 10)
		vy = random.randint(3, 10)
		r.append(MyRectangle(random.randint(0, MyScreen.width - 40), random.randint(0, MyScreen.height - 40), l, l, vx , vy))
	return r


FPS = 20
MyScreen.width = 900
MyScreen.height = 600


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 30)


screen = pygame.display.set_mode((int(MyScreen.width * 1.45), MyScreen.height))
clock = pygame.time.Clock()


arrayDetection = Collision_detection_Array()
arrayStop = Stopwatch()
arrayLabel = myfont.render("Array based", False, MyColor.white)

hashDetection = Collision_Detection_Spatial_hashing()
hashStop = Stopwatch()
hashLabel = myfont.render("Hash based", False, MyColor.white)


loop = True


r = GetRandomRects(100)

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
	arrayTimeNum = arrayStop.time_elapsed()
	arrayTime = myfont.render(str(arrayTimeNum)  + ' ms', False, MyColor.white)
	arrayStop.reset()

	hashStop.start()
	hashResult = hashDetection.CheckCollisions(r)
	hashStop.stop()
	hashTimeNum = hashStop.time_elapsed()
	hashTime = myfont.render(str(hashTimeNum) + ' ms  ~' + str(arrayTimeNum//max(hashTimeNum, 1)) + " Times Faster", False, MyColor.white)
	hashStop.reset()

	# if not arrayResult == hashResult:
		# print( "fail ")
		# print(arrayResult)
		# print(hashResult)

	screen.fill((MyColor.black))
	
	for i in r:
		pygame.draw.rect(screen, (255,255,255), i.GetBounds(), 0)

	screen.blit(arrayLabel,(MyScreen.width * 1.05, 0))
	screen.blit(arrayTime,(MyScreen.width * 1.05, 30))
	screen.blit(hashLabel,(MyScreen.width * 1.05, 60))
	screen.blit(hashTime,(MyScreen.width * 1.05, 90))

	pygame.display.flip()
	
	clock.tick(FPS)

	b = pygame.time.get_ticks()

	if a-b > 1.5/FPS:
		print(a-b)
	
pygame.quit()

