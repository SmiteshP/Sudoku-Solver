# Sudoku-Solver

create the Grid instance by giving it a list of lists, 
each inner list represents a row of the puzzle
enter 0 inplace of empty places to be solved
Example :-
		Grid([
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

This code can only solve the board if it has a unique solution
Also the validity of the initial game board is NOT checked 
and is assumed to be correct.

No fancy algorithm is used to solve the game board, each 
tile is individually checked if its number can be deduced 
over and over again until the board is solved or no
further progress can be made.
