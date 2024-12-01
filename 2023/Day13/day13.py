from collections import Counter
import os
import sys
import math
sys.setrecursionlimit(10000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

def isColReflection(grid, col):
	for row in grid:
		l, r = col, col + 1
		while l >= 0 and r < len(row):
			if row[l] != row[r]:
				return False
			l -= 1
			r += 1
	return True


def isRowReflection(grid, row):
	top, bottom = row, row + 1
	while top >= 0 and bottom < len(grid):
		for j in range(len(grid[row])):
			if grid[top][j] != grid[bottom][j]:
				return False
		top -= 1
		bottom += 1
	return True
	
def part1():
	blocks = []
	with open("input.txt", "r") as fp:
		blocks = fp.read().split("\n\n")
	
	col = 0
	row = 0
	for block in blocks:
		grid = block.strip().splitlines()
		for j in range(len(grid[0]) - 1):
			if isColReflection(grid, j):
				col += j + 1
				break 
		
		for i in range(len(grid) - 1):
			if isRowReflection(grid, i):
				row += i + 1
				break
	
	return row * 100 + col 
		


def part2():
	blocks = []
	with open("input.txt", "r") as fp:
		blocks = fp.read().split("\n\n")

	col = 0
	row = 0
	for block in blocks:
		grid = block.strip().splitlines()
		grid = [[ch for ch in row] for row in grid]
		old_R = 0 
		old_C = 0
		for j in range(len(grid[0]) - 1):
			if isColReflection(grid, j):
				old_C = j + 1
				break
		
		for i in range(len(grid) - 1):
			if isRowReflection(grid, i):
				old_R = i + 1
				break
	
		new_C = 0 
		new_R = 0
		for i in range(len(grid)):
			if new_C + new_R > 0:
				break
			for j in range(len(grid[0])):
				if new_C + new_R > 0:
					break 
				old = grid[i][j]
				grid[i][j] = "#" if old == "." else "."
				for k in range(len(grid[0]) - 1):
					if k + 1 != old_C and isColReflection(grid, k):
						new_C = k + 1
						col += k + 1
						break
		
				for k in range(len(grid) - 1):
					if k + 1 != old_R and isRowReflection(grid, k):
						new_R = k + 1
						row += k + 1
						break

				grid[i][j] = old

	return row * 100 + col 

if __name__ == "__main__":
	# print(part1())
	print(part2())
