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

NORTH = (-1, 0)
SOUTH = (1, 0)
WEST = (0, -1)
EAST = (0, 1)

MP = {
	"." : {NORTH: [NORTH], SOUTH : [SOUTH], WEST: [WEST], EAST : [EAST]},
	"|" : {NORTH: [NORTH], SOUTH: [SOUTH], WEST: [SOUTH, NORTH], EAST : [SOUTH, NORTH]},
	"/": 	{NORTH: [EAST], SOUTH: [WEST], WEST: [SOUTH], EAST: [NORTH]},
	"\\": {NORTH: [WEST], SOUTH: [EAST], WEST: [NORTH], EAST: [SOUTH]},
	"-": 	{NORTH: [WEST, EAST], SOUTH: [WEST, EAST], WEST: [WEST], EAST : [EAST]},
}

def solve(grid, x, y, dir):
	visited = {(x, y, dir)}
	stk = [(x, y, dir)]
	n = len(grid)
	m = len(grid[0])
	marked = [[0 for _ in range(m)] for _ in range(n)]
	while stk:
		x, y, dir = stk.pop()
		marked[x][y] = 1
		for dx, dy in MP[grid[x][y]][dir]:
			nx, ny = x + dx, y + dy
			if 0 <= nx < n and 0 <= ny < m and (nx, ny, (dx, dy)) not in visited:
				stk.append((nx, ny, (dx, dy)))
				visited.add((nx, ny, (dx, dy)))
	
	return sum([x for row in marked for x  in row])

def part1():
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().splitlines()

	return solve(grid, 0, 0, EAST)

def part2():
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().splitlines()
	
	n, m = len(grid), len(grid[0])
	ans = 0
	for j in range(m):
		ans = max(ans, solve(grid, 0, j, SOUTH))
		ans = max(ans, solve(grid, n - 1, j, NORTH))
	
	for i in range(n):
		ans = max(ans, solve(grid, i, 0, EAST))
		ans = max(ans, solve(grid, i, m - 1, WEST))
	return ans

if __name__ == "__main__":
	print(part1())
	print(part2())
