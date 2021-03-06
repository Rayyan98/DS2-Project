# Bigger imports
import pygame
import random
import math

# Smaller imports
from MyRectangle import MyRectangle
from MyColor import MyColor
from MyScreen import MyScreen
from stopwatch import Stopwatch


# Algorithm imports
from Collision_detection_Array import Collision_detection_Array
from SpatialHashing import Collision_Detection_Spatial_hashing
from Skiplist import Collision_Detection_SkipList
from QuadTree import Collision_Detection_Quad_Tree
from BinaryTree import Collision_Detection_Binary_Tree
from AABBTrees import Collision_detection_AABB

def GetRandomRects(n):
	r = []
	for i in range(n):
		l= random.randint(3,10)
		vx = random.randint(3, 10)
		vy = random.randint(3, 10)
		r.append(MyRectangle(random.randint(0, MyScreen.width - 40), random.randint(0, MyScreen.height - 40), l, l, vx , vy))
	return r


FPS = 20
MyScreen.width = 900
MyScreen.height = 600


pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Calibri', 30)


screen = pygame.display.set_mode((int(MyScreen.width * 1.45), MyScreen.height))
clock = pygame.time.Clock()


arrayDetection = Collision_detection_Array()
arrayStop = Stopwatch()
arrayLabel = myfont.render("Array based", False, MyColor.white)

hashDetection = Collision_Detection_Spatial_hashing()
hashStop = Stopwatch()
hashLabel = myfont.render("Hash based", False, MyColor.white)

skipDetection = Collision_Detection_SkipList()
skipStop = Stopwatch()
skipLabel = myfont.render("Skiplist based", False, MyColor.white)

quadDetection = Collision_Detection_Quad_Tree()
quadStop = Stopwatch()
quadLabel = myfont.render("QuadTree based", False, MyColor.white)

aabbDetection = Collision_detection_AABB()
aabbStop = Stopwatch()
aabbLabel = myfont.render("AABBTree based", False, MyColor.white)

binDetection = Collision_Detection_Binary_Tree()
binStop = Stopwatch()
binLabel = myfont.render("BinaryTree based", False, MyColor.white)


loop = True


r = GetRandomRects(300)

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



        screen.fill((MyColor.black))

        for i in r:
                pygame.draw.rect(screen, (255,255,255), i.GetBounds(), 0)

        arrayStop.start()
        arrayResult = arrayDetection.CheckCollisions(r)
        arrayStop.stop()
        arrayTimeNum = arrayStop.time_elapsed()
        arrayTime = myfont.render(str(arrayTimeNum)  + ' ms', False, MyColor.white)
        arrayStop.reset()
        screen.blit(arrayLabel,(MyScreen.width * 1.05, 0))
        screen.blit(arrayTime,(MyScreen.width * 1.05, 30))

        hashStop.start()
        hashResult = hashDetection.CheckCollisions(r)
        hashStop.stop()
        hashTimeNum = hashStop.time_elapsed()
        hashTime = myfont.render(str(hashTimeNum) + ' ms  ~' + str(math.ceil(arrayTimeNum/max(hashTimeNum, 1))) + " Times Faster", False, MyColor.white)
        hashStop.reset()
        screen.blit(hashLabel,(MyScreen.width * 1.05, 60))
        screen.blit(hashTime,(MyScreen.width * 1.05, 90))

        skipStop.start()
        skipResult = skipDetection.CheckCollisions(r)
        skipStop.stop()
        skipTimeNum = skipStop.time_elapsed()
        skipTime = myfont.render(str(skipTimeNum) + ' ms  ~' + str(math.ceil(arrayTimeNum/max(skipTimeNum, 1))) + " Times Faster", False, MyColor.white)
        skipStop.reset()
        screen.blit(skipLabel,(MyScreen.width * 1.05, 120))
        screen.blit(skipTime,(MyScreen.width * 1.05, 150))

        quadStop.start()
        quadResult = quadDetection.CheckCollisions(r)
        quadStop.stop()
        quadTimeNum = quadStop.time_elapsed()
        quadTime = myfont.render(str(quadTimeNum) + ' ms  ~' + str(math.ceil(arrayTimeNum/max(quadTimeNum, 1))) + " Times Faster", False, MyColor.white)
        quadStop.reset()
        screen.blit(quadLabel,(MyScreen.width * 1.05, 180))
        screen.blit(quadTime,(MyScreen.width * 1.05, 210))

        binStop.start()
        binResult = binDetection.CheckCollisions(r)
        binStop.stop()
        binTimeNum = binStop.time_elapsed()
        binTime = myfont.render(str(binTimeNum) + ' ms  ~' + str(math.ceil(arrayTimeNum/max(binTimeNum, 1))) + " Times Faster", False, MyColor.white)
        binStop.reset()
        screen.blit(binLabel,(MyScreen.width * 1.05, 240))
        screen.blit(binTime,(MyScreen.width * 1.05, 270))


        # aabbStop.start()
        # aabbResult = aabbDetection.CheckCollisions(r)
        # aabbStop.stop()
        # aabbTimeNum = aabbStop.time_elapsed()
        # aabbTime = myfont.render(str(aabbTimeNum) + ' ms  ~' + str(math.ceil(arrayTimeNum//max(aabbTimeNum, 1))) + " Times Faster", False, MyColor.white)
        # aabbStop.reset()
        # screen.blit(aabbLabel,(MyScreen.width * 1.05, 300))
        # screen.blit(aabbTime,(MyScreen.width * 1.05, 330))



        if not arrayResult == skipResult:
                print("fail skip")
        if not arrayResult == hashResult:
                print("fail hash")
        if not arrayResult == quadResult:
                print("fail quad")
                print(quadResult)
        if not arrayResult == binResult:
                print("fail aabb")

		 
        pygame.display.flip()

        clock.tick(FPS)

        b = pygame.time.get_ticks()

        if a-b > 1.5/FPS:
                print(a-b)

pygame.quit()

