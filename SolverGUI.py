from tkinter import *

class Board_Input:
	'''
	Class to create input space for sudoku.

	'''

	def __init__(self, root):
		self.root = root

		self.inTiles = []
		for y in range(9):
			self.inTiles.append([Entry(self.root, width=3) for x in range(9)])

	def placeBoard(self, row, col):
		for y, r in enumerate(self.inTiles):
			for x, inTile in enumerate(r):
				# skip row 3 and 7 to be used as spacer
				if y < 3:
					rSpacer = 0
				elif y < 6:
					rSpacer = 1
				else:
					rSpacer = 2

				# skip coloumn 3 and 7 to be used as spacer
				if x < 3:
					cSpacer = 0
				elif x < 6:
					cSpacer = 1
				else:
					cSpacer = 2

				inTile.grid(row=y+row+rSpacer, column=x+col+cSpacer, padx=1, pady=1)


		# create some space in between the rows
		rowSpacer1 = Label(self.root)
		rowSpacer1.grid(row=3+row, column=col)

		rowSpacer2 = Label(self.root)
		rowSpacer2.grid(row=7+row, column=col)

		# create some space in between the columns
		colSpacer1 = Label(self.root, text=" ")
		colSpacer1.grid(row=row, column=3+col)

		colSpacer2 = Label(self.root, text=" ")
		colSpacer2.grid(row=row, column=7+col)

	def getInput(self):
		# Returns all the entered values

		currentBoard = []

		for row in self.inTiles:
			currentBoard.append([int(inTile.get()) if inTile.get() != '' else 0 for inTile in row])

		return currentBoard

def displayBoard(root, board):

	text = ''
	for j, row in enumerate(board):
			for i, num in enumerate(row):
				if i%3 == 0 and i != 0:
					text += '\t'+num+' '
				else:
					text += num+' '
			if (j+1)%3 == 0 and j != 0:
				text += '\n\n'
			else:
				text += '\n'

	solution = Label(root, text=text)
	solution.pack()
