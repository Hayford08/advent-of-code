from collections import Counter
from collections import deque
import os
import sys
import math
sys.setrecursionlimit(10000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

TARGET = 1000000000

def tilt_platform(grid):
	for j in range(len(grid[0])):
		q = deque([])
		for i in range(len(grid)):
			if grid[i][j] == "O":
				if len(q):
					x, y = q.popleft()
					grid[x][y] = "O"
					grid[i][j] = "."
					q.append((i, j))
			elif grid[i][j] == ".":
				q.append((i, j))
			else:
				q = deque([])

def calculate(grid):
	ans = 0
	for i, row in enumerate(grid):
		cnt = 0
		for ch in row:
			if ch == "O":
				cnt += 1
		ans += (len(grid) - i) * cnt
	return ans


def part1():
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().splitlines()
		grid = [[ch for ch in row] for row in grid]
	
	tilt_platform(grid)
	return calculate(grid)

def part2():
	def rotate_90_cw(grid):
		N = len(grid)
		for i in range((N + 1) // 2):
				for j in range(N // 2):
						grid[i][j], grid[N - j - 1][i], grid[N - i - 1][N - j - 1], grid[j][N - i - 1] = \
						grid[N - j - 1][i], grid[N - i - 1][N - j - 1], grid[j][N - i - 1], grid[i][j]

	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().splitlines()
		grid = [[ch for ch in row] for row in grid]

	key = tuple(tuple(row) for row in grid)
	grid_to_cycle_num = {key : 0}
	cycle_num_to_grid = {0 : key}
	cnt = 0
	while True:
		cnt += 1
		for _ in range(4):
			tilt_platform(grid)
			rotate_90_cw(grid)

		key = tuple(tuple(row) for row in grid)
		if key in grid_to_cycle_num:
			break

		grid_to_cycle_num[key] = cnt
		cycle_num_to_grid[cnt] = key
		
	start_num = grid_to_cycle_num[key]
	cycle_len = cnt - start_num
	
	target_num = (TARGET - start_num) % cycle_len + start_num
	return calculate(cycle_num_to_grid[target_num])

if __name__ == "__main__":
	# print(part1())
	print(part2())
