class Grid():

	def __init__(self, StartingGrid):
		self.grid = StartingGrid

	class Tile():

		def __init__(self, x, y, val = 0):
			self.x = x
			self.y = y
			self.val = val

	class RowInfo():

		def __init__(self, rowNumber):
			pass

	class ColInfo():

		def __init__(self, colNumber):
			pass

	class BoxInfo():

		def __init__(self):
			pass
			