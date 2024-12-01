from collections import Counter
from collections import deque
import sys 
import os
import math
sys.setrecursionlimit(10000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass
NORTH = (-1, 0)
SOUTH = (1, 0)
EAST = (0, 1)
WEST = (0, -1)

MP = {
	"|" : [NORTH, SOUTH],
	"-": [EAST, WEST],
	"L": [NORTH, EAST],
	"J": [NORTH, WEST],
	"7": [SOUTH, WEST],
	"F": [SOUTH, EAST],
	"S": [NORTH, SOUTH, EAST, WEST],
	".": []
}

def get_neighbors(grid, r, c):
	res = []
	ch = grid[r][c]
	if ch == "S":
		for dx, dy in MP[ch]:
			nr, nc = r + dx, c + dy 
			if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
				for dx2, dy2 in MP[grid[nr][nc]]:
					nr2, nc2 = nr + dx2, nc + dy2 
					if 0 <= nr2 < len(grid) and 0 <= nc < len(grid[r]) and grid[nr2][nc2] == "S":
						res.append((nr, nc))
						break
	else:
		for dx, dy in MP[grid[r][c]]:
			nr, nc = r + dx, c + dy
			if 0 <= nr < len(grid) and 0 <= nc < len(grid[r]):
				res.append((nr, nc))
	return res
	
def part1():
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().strip().splitlines()

	sx, sy = None, None 
	for i, row in enumerate(grid):
		if sx is not None:
			break 
		for j, ch in enumerate(row):
			if ch == 'S':
				sx, sy = i, j
				break 
	

	ans = -1
	seen = {(sx, sy)}
	stk = [(sx,sy)]
	while stk:
		new_stk = []
		ans += 1
		for x, y in stk:
			ch = grid[x][y]
			for nei in get_neighbors(grid, x, y):
				if nei not in seen:
					seen.add(nei)
					new_stk.append(nei)
		stk = new_stk
	return ans

def part2():
	LOOP = "SLFJ7-|"
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().strip().splitlines()
	
	n, m = len(grid), len(grid[0])
	visited = set()

	def create_loop():
		sx, sy = None, None 
		for i, row in enumerate(grid):
			if sx is not None:
				break 
			for j, ch in enumerate(row):
				if ch == 'S':
					sx, sy = i, j
					break
		visited.add((sx, sy))

		q = deque([(sx, sy)])
		while q:
			x, y = q.popleft()
			for nei in get_neighbors(grid, x, y):
				if nei not in visited:
					visited.add(nei)
					q.append(nei)
	
	def count_edge_crosings(x, y):
		EDGES = "L|J"
		row = grid[x]
		cnt = 0
		for j in range(y):
			if (x, j) not in visited or row[j] not in EDGES:
				continue
			cnt += 1
		return cnt 

	create_loop()
	ans = 0
	for i in range(n):
		for j in range(m):
			if (i, j) not in visited and count_edge_crosings(i, j) % 2 == 1:
				ans += 1
	return ans

if __name__ == "__main__":
	# print(part1())
	print(part2())
