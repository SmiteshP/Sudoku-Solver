class Grid():
# Grid holds all the data of the gameboard

	def __init__(self, StartingGrid):
		
		self.grid = StartingGrid
		
		# rowList contains all the sets that numbers contained in that row
		self.rowList = []
		for y in range(1, 10):
			self.rowList.append({self.grid[y-1][k] for k in range(9)})

		# colList contains all the sets that numbers contained in that coloumn
		self.colList = []
		for x in range(1, 10):
			self.colList.append({self.grid[k][x-1] for k in range(9)})

		# boxList contains all the sets that numbers contained in that box
		self.boxList = []
		for y in range(0, 9, 3):
			for x in range(0, 9, 3):
				temp = set()
				for j in range(3):
					for i in range(3):
						temp.add(self.grid[y+j][x+i])
				self.boxList.append(temp)

		# tileList contians all the tile objects
		self.tileList = []
		for y in range(1, 10):
			for x in range(1, 10):
				self.tileList.append(self.Tile(x, y, self))

	class Tile():
		'''
		A grid is made up of 81 individual tiles
		Each tile is capable of solving for itself by
		checking the values in its row, coloumn and box

		'''

		def __init__(self, x, y, containerGrid):
			self.x = x
			self.y = y
			self.val = containerGrid.grid[y-1][x-1]
			self.rowSet = containerGrid.rowList[y-1]
			self.colSet = containerGrid.colList[x-1]
			self.boxSet = containerGrid.boxList[Grid.getBoxNum(x, y) - 1]

		def isSolved(self):
		# Return true when solved, else false
			if self.val != 0:
				return True
			else:
				return False

		def solve(self):

			# unionSet contains all the numbers that the tile cannot take
			unionSet = self.rowSet.union(self.colSet, self.boxSet)
			
			if (len(unionSet) == 9) and (0 in unionSet) and (not self.isSolved()):
				for num in range(1, 10):
					if num not in unionSet:
						self.val = num
						self.rowSet.add(num)
						self.colSet.add(num)
						self.boxSet.add(num)
			
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

	def printGrid(self):

		'''
		prints the grid in a nice format
		
		'''

		self.updateGrid()
		
		for j, row in enumerate(self.grid):
			for i, num in enumerate(row):
				if i%3 == 0 and i != 0:
					print('\t', num, end = ' ')
				else:
					print(num, end = ' ')
			if (j+1)%3 == 0 and j != 0:
				print()
				print()
			else:
				print()

	def updateGrid(self):
		for tile in self.tileList:
			self.grid[tile.y - 1][tile.x - 1] = tile.val

	def numSolvedTiles(self):
		return len([tile for tile in self.tileList if tile.isSolved()])

	def solve(self):

		numSolvedBefore = 0

		while(numSolvedBefore < self.numSolvedTiles()):
			numSolvedBefore = self.numSolvedTiles()

			for tile in self.tileList:
				if not tile.isSolved():
					tile.solve()