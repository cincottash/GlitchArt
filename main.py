from setup import *
import random
import math

#length/width in pixels of our block
blockPixelSize = 50

#Making temp block for use later with dummy value x
tempBlock = [[] for _ in range(blockPixelSize)]
for i in range(blockPixelSize):
	for j in range(blockPixelSize):
		tempBlock[i].append("x")
		
#swaps blockA and blockB, provided that it is possible to swap them
def swapBlocks(blockA, blockB):
	#the coord of where our block starts
	blockAPixelStart = [blockPixelSize*blockA[0], blockPixelSize*blockA[1]]

	blockBPixelStart = [blockPixelSize*blockB[0], blockPixelSize*blockB[1]]

	#Copy blockA into a temp block and overwrite it with block B
	for i in range(blockPixelSize):
		for j in range(blockPixelSize):
			#copy A to temp
			tempBlock[i][j] = canvas.get_at((blockAPixelStart[0]+i,blockAPixelStart[1]+j))
			#overwrite A with the corresponding colors at B
			color = canvas.get_at((blockBPixelStart[0]+i, blockBPixelStart[1]+j))
			canvas.set_at((blockAPixelStart[0]+i, blockAPixelStart[1]+j), color)

	#Copy temp(blockA) into blockB
	for i in range(blockPixelSize):
		for j in range(blockPixelSize):
			color = tempBlock[i][j]
			canvas.set_at((blockBPixelStart[0]+i, blockBPixelStart[1]+j), color)

def getRGBavg(block):
	totalR = 0
	totalG = 0
	totalB = 0
	
	blockPixelStart = [blockPixelSize*block[0], blockPixelSize*block[1]]
	
	for i in range(blockPixelSize):
		for j in range(blockPixelSize):
			color = canvas.get_at((blockPixelStart[0]+i, blockPixelStart[1]+j))
			totalR += color[0]
			totalG += color[1]
			totalB += color[2]

	averageR = totalR/blockPixelSize**2
	averageG = totalG/blockPixelSize**2
	averageB = totalB/blockPixelSize**2


	return averageR, averageG, averageB 

def main():
	while(True):
		maxBlocks = canvasSize/blockPixelSize-1

		#only swaps blocks which are exactly 1 distance apart
		canSwap = False
		while(canSwap == False):

			blockA = [random.randint(0, maxBlocks), random.randint(0, maxBlocks)]
			blockB = [random.randint(0, maxBlocks), random.randint(0, maxBlocks)]

			#Get average RGB value of block A and B
			blockAavgR,  blockAavgG, blockAavgB = getRGBavg(blockA)
			
			blockBavgR,  blockBavgG, blockBavgB = getRGBavg(blockB)

			print(blockAavgR)

			canSwap = True



		
		pygame.display.update()


if __name__ == '__main__':
	main()

#Surface.get_at((x, y)): return pixel Color
#surface.set_at((x, y), color) set pixel color