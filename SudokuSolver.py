class Grid():
# Grid holds all the data of the gameboard

	def __init__(self, StartingGrid):
		
		self.grid = StartingGrid
	
		# tileList contians all the tile objects
		self.tileList = []
		for y in range(1, 10):
			for x in range(1, 10):
				self.tileList.append(self.Tile(x, y, self.grid[y-1][x-1]))
		
		# rowList contains all the ComponentInfo objects that store info about Rows
		self.rowList = []
		for y in range(1, 10):
			temp = {self.grid[y-1][k] for k in range(9)}
			self.rowList.append(self.ComponentInfo(y, temp))

		# colList contains all the ComponentInfo objects that store info about Cols
		self.colList = []
		for x in range(1, 10):
			temp = {self.grid[k][x-1] for k in range(9)}
			self.colList.append(self.ComponentInfo(x, temp))

		# boxList contains all the ComponentInfo objects that store info about Boxes
		self.boxList = []
		for i in range(1, 10):
			self.boxList.append(self.ComponentInfo(i, temp))

	class Tile():

		def __init__(self, x, y, val = 0):
			self.x = x
			self.y = y
			self.val = val
			self.box = Grid.getBoxNum(x, y)

	class ComponentInfo():

		def __init__(self, compNumber, initialInfo):
			self.index = compNumber
			self.numsSet = initialInfo

			
	@staticmethod
	def getBoxNum(x, y):

		'''
		returns box number for given x y of the tile

		1 2 3
		4 5 6
		7 8 9

		'''

		boxNums = [1, 1, 1, 2, 2, 2, 3, 3, 3]
		
		if y >= 1 and y <= 3:
			return boxNums[x-1]
		elif y >= 4 and y <= 6:
			return boxNums[x-1] + 3
		else:
			return boxNums[x-1] + 6