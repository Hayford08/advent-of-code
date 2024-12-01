from collections import deque
import os
import sys
import math
sys.setrecursionlimit(20000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

DIR = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def part1():
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().strip().splitlines()
	
	n, m = len(grid), len(grid[0])
	sx, sy = None, None 
	for i, row in enumerate(grid):
		if sx is not None:
			break
		for j, ch in enumerate(row):
			if ch == "S":
				sx, sy = i, j
				break

	q = deque([(sx, sy, 0)])
	seen = set((sx, sy))
	ans = set()
	while q:
		x, y, steps = q.popleft()
		if steps > 64:
			continue
		if steps % 2 == 0:
			ans.add((x, y))

		for dx, dy in DIR:
			nx, ny = x + dx, y + dy
			if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != "#" and (nx, ny) not in seen:
				q.append((nx, ny, steps + 1))
				seen.add((nx, ny))
	return len(ans)


def part2():
	pass 
	# still learning the trick 
	# but this video explains a lot: https://www.youtube.com/watch?v=9UOMZSL0JTg
	

if __name__ == "__main__":
	print(part1())
	print(part2())
