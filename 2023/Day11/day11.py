import os
import sys

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

GALAZY = "#"

def part1():
	SCALE = 2
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().strip().splitlines()
	
	n = len(grid)
	m = len(grid[0])
	row_count, column_count = [0 for _ in range(n)], [0 for _ in range(m)]
	galaxies = []
	for i, row in enumerate(grid):
		for j, ch in enumerate(row):
			if ch == GALAZY:
				galaxies.append((i, j))
				row_count[i] += 1
				column_count[j] += 1
	
	ans = 0
	for i, (r1, c1) in enumerate(galaxies):
		for (r2, c2) in galaxies[:i]:
			for row in range(min(r1, r2), max(r1, r2)):
				ans += 1 if row_count[row] != 0 else SCALE
			for col in range(min(c1, c2), max(c1, c2)):
				ans += 1 if column_count[col] != 0 else SCALE
	return ans

def part2():
	SCALE = 1000000
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().strip().splitlines()
	
	n = len(grid)
	m = len(grid[0])
	row_count, column_count = [0 for _ in range(n)], [0 for _ in range(m)]
	galaxies = []
	for i, row in enumerate(grid):
		for j, ch in enumerate(row):
			if ch == GALAZY:
				galaxies.append((i, j))
				row_count[i] += 1
				column_count[j] += 1
	
	ans = 0
	for i, (r1, c1) in enumerate(galaxies):
		for (r2, c2) in galaxies[:i]:
			for row in range(min(r1, r2), max(r1, r2)):
				ans += 1 if row_count[row] != 0 else SCALE
			for col in range(min(c1, c2), max(c1, c2)):
				ans += 1 if column_count[col] != 0 else SCALE
	return ans

if __name__ == "__main__":
	# print(part1())
	print(part2())
