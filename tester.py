from SudokuSolver import *

game = Grid([
				[0, 0, 2,  8, 7, 0,  0, 0, 0],
				[7, 0, 0,  0, 0, 4,  6, 0, 0],
				[6, 4, 3,  9, 0, 0,  0, 7, 0],

				[5, 2, 6,  1, 0, 0,  8, 9, 0],
				[0, 0, 0,  0, 8, 0,  0, 0, 0],
				[0, 9, 8,  0, 0, 2,  1, 6, 3],

				[0, 1, 0,  0, 0, 7,  9, 3, 2],
				[0, 0, 4,  3, 0, 0,  0, 0, 5],
				[0, 0, 0,  0, 9, 8,  4, 0, 0]
			])

print("Initial GameBoard:-\n")
game.printGrid()

game.solve()

print("\nFinal Solution:-\n")
game.printGrid()