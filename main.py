from SolverGUI import *
from SudokuSolver import *
import os

root = Tk()
root.title("Sudoku Solver")

### Fuctions ###

def solve():

	puzzle = inBoard.getInput()

	board = Grid(puzzle)
	board.solve()
	
	os.system('clear')
	print("Solution is :- \n")
	board.printGrid()

def clear():
	
	for row in inBoard.inTiles:
		for inTile in row:
			inTile.delete(0, END)

### Create GUI ###

inBoard = Board_Input(root)
Solve = Button(root, text="Solve", command=solve)
Clear = Button(root, text="Clear", command=clear)

### Display GUI ###

inBoard.placeBoard(0, 0)
Solve.grid(row=20, column=0, columnspan=2)
Clear.grid(row=20, column=4, columnspan=2)

root.mainloop()