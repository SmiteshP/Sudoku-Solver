class Grid():
# Grid holds all the data of the gameboard

	def __init__(self, StartingGrid):
		
		self.grid = StartingGrid
	
		# tileList contians all the tile objects	
		self.tileList = []
		for y in range(1, 10):
			for x in range(1, 10):
				self.tileList.append(Tile(x, y, grid[x-1][y-1]))
		
		# rowList contains all the ComponentInfo objects that store info about Rows
		self.rowList = []
		for y in range(1, 10):
			self.rowList.append(ComponentInfo(y))

		# colList contains all the ComponentInfo objects that store info about Cols
		self.colList = []
		for x in range(1, 10):
			self.colList.append(ComponentInfo(x))

		# boxList contains all the ComponentInfo objects that store info about Boxes
		self.boxList = []
		for i in range(1, 10):
			self.boxList.append(ComponentInfo(i))

	class Tile():

		def __init__(self, x, y, val = 0):
			self.x = x
			self.y = y
			self.val = val
			self.box = Grid.getBoxNum(x, y)

	class ComponentInfo():

		def __init__(self, compNumber):
			
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
			return boxNums[x]
		elif y >= 4 and y <= 6:
			return boxNums[x] + 3
		else:
			return boxNums[x] + 6