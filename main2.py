# Bigger imports
import random
import math

# Smaller imports
from MyRectangle import MyRectangle
from MyColor import MyColor
from MyScreen import MyScreen
from stopwatch import Stopwatch
import matplotlib.pyplot as plt

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


def CheckTimesForN(n):

	times  = []
	arrayDetection = Collision_detection_Array()
	arrayStop = Stopwatch()

	hashDetection = Collision_Detection_Spatial_hashing()
	hashStop = Stopwatch()

	skipDetection = Collision_Detection_SkipList()
	skipStop = Stopwatch()

	quadDetection = Collision_Detection_Quad_Tree()
	quadStop = Stopwatch()

	aabbDetection = Collision_detection_AABB()
	aabbStop = Stopwatch()

	binDetection = Collision_Detection_Binary_Tree()
	binStop = Stopwatch()


	r = GetRandomRects(n)
	arrayStop.start()
	arrayResult = arrayDetection.CheckCollisions(r)
	arrayStop.stop()
	arrayTimeNum = arrayStop.time_elapsed()
	times.append(arrayTimeNum)
	arrayStop.reset()

	hashStop.start()
	hashResult = hashDetection.CheckCollisions(r)
	hashStop.stop()
	hashTimeNum = hashStop.time_elapsed()
	times.append(hashTimeNum)
	hashStop.reset()

	skipStop.start()
	skipResult = skipDetection.CheckCollisions(r)
	skipStop.stop()
	skipTimeNum = skipStop.time_elapsed()
	times.append(skipTimeNum)
	skipStop.reset()

	quadStop.start()
	quadResult = quadDetection.CheckCollisions(r)
	quadStop.stop()
	quadTimeNum = quadStop.time_elapsed()
	times.append(quadTimeNum)
	quadStop.reset()

	binStop.start()
	binResult = binDetection.CheckCollisions(r)
	binStop.stop()
	binTimeNum = binStop.time_elapsed()
	times.append(binTimeNum)
	binStop.reset()


	# aabbStop.start()
	# aabbResult = aabbDetection.CheckCollisions(r)
	# aabbStop.stop()
	# aabbTimeNum = aabbStop.time_elapsed()
	# times.append(aabbTimeNum)
	# aabbStop.reset()

	return times
	
	
n = [100,200,500,1000,2000,5000,10000]
Times = [[] for i in range(5)]

for i in n:
	t = CheckTimesForN(i)
	for i in range(len(t)):
		Times[i].append(t[i])
		
	print(Times)
	

s = ['Array' , 'Hash', 'SkipList', 'QuadTree', 'BinTree']
col = ['r','b','g','c','m']

for i in range(len(Times)):
	plt.plot(n,Times[i], col[i], label = s[i])
	
plt.legend(loc = 'upper left')

plt.show()

	
	