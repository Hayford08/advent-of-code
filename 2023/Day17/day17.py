from collections import Counter
from heapq import heappop, heappush
import os
import sys
sys.setrecursionlimit(10000)

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
	grid = [[int(val) for val in row] for row in grid]

	n = len(grid)
	m = len(grid[0])
	min_heap = [(0, 0, 0, 0, 0, 0)]
	seen = set()
	while min_heap:
		cost, x, y, dx, dy, cnt = heappop(min_heap)

		if x == n - 1 and y == m - 1:
			return cost
		
		if (x, y, dx, dy, cnt) in seen:
			continue 

		seen.add((x, y, dx, dy, cnt))

		for ndx, ndy in DIR:
			if (ndx, ndy) == (-dx, -dy):
				continue
			nx, ny = x + ndx, y + ndy
			if 0 <= nx < n and 0 <= ny < m:
				if (ndx, ndy) == (dx, dy) and cnt < 3:
					heappush(min_heap, (cost + grid[nx][ny], nx, ny, ndx, ndy, cnt + 1))
				elif (ndx, ndy) != (dx, dy):
					heappush(min_heap, (cost + grid[nx][ny], nx, ny, ndx, ndy, 1))

	return -1

def part2():
	grid = []
	with open("input.txt", "r") as fp:
		for row in fp.readlines():
			grid.append([int(ch) for ch in row.strip()])
	
	n = len(grid)
	m = len(grid[0])
	min_heap = [(0, 0, 0, 0, 0, 0)]
	seen = set()
	while min_heap:
		cost, x, y, dx, dy, cnt = heappop(min_heap)

		if x == n - 1 and y == m - 1 and cnt > 3:
			return cost
		
		if (x, y, dx, dy, cnt) in seen:
			continue

		seen.add((x, y, dx, dy, cnt))

		for ndx, ndy in DIR:
			if (ndx, ndy) == (-dx, -dy):
				continue
			nx, ny = x + ndx, y + ndy
			if 0 <= nx < n and 0 <= ny < m:
				if (ndx, ndy) == (dx, dy) and cnt < 10:
					heappush(min_heap, (cost + grid[nx][ny], nx, ny, ndx, ndy, cnt + 1))
				elif (cnt > 3 or (x == 0 and y == 0)) and (ndx, ndy) != (dx, dy):
					heappush(min_heap, (cost + grid[nx][ny], nx, ny, ndx, ndy, 1))

	return -1


if __name__ == "__main__":
	# print(part1())
	print(part2())
