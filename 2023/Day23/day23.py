from collections import Counter, deque, defaultdict
import os
import sys
import math
sys.setrecursionlimit(20000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

DIR1 = {
	"^" : [(-1, 0)],
	"v" : [(1, 0)],
	"<"	: [(0, -1)],
	">"	: [(0, 1)],
	"."	: [(-1, 0), (1, 0), (0, 1), (0, -1)],
}

DIR2 = {
	"^" : [(-1, 0), (1, 0), (0, 1), (0, -1)],
	"v" : [(-1, 0), (1, 0), (0, 1), (0, -1)],
	"<"	: [(-1, 0), (1, 0), (0, 1), (0, -1)],
	">"	: [(-1, 0), (1, 0), (0, 1), (0, -1)],
	"."	: [(-1, 0), (1, 0), (0, 1), (0, -1)],
}

def points_of_interest(grid, start, end):
	n = len(grid)
	m = len(grid[0])
	res = set([start, end])
	for i, row in enumerate(grid):
		for j, ch in enumerate(row):
			if ch == "#":
				continue
			neighbors = 0
			for dx, dy in DIR1["."]:
				nx, ny = i + dx, j + dy
				if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != "#":
					neighbors += 1
			
			if neighbors >= 3:
				res.add((i, j))
	return res

def construct_graph(grid, points, dir): # path contraction
	graph = {pt: {} for pt in points}
	n, m = len(grid), len(grid[0])
	for sx, sy in points:
		stk = [(sx, sy, 0)]
		visited = [[False for _ in range(m)] for _ in range(n)]
		visited[sx][sy] = True

		while stk:
			x, y, cnt = stk.pop()
			if cnt != 0 and (x, y) in points:
				graph[(sx, sy)][(x, y)] = cnt
				continue
			
			for dx, dy in dir[grid[x][y]]:
				nx, ny = x + dx, y + dy
				if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != "#" and not visited[nx][ny]:
					stk.append((nx, ny, cnt + 1))
					visited[nx][ny] = True

	return graph

def part1():
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().strip().splitlines()
	n = len(grid)
	m = len(grid[0])
	start = (0, grid[0].find("."))
	end = (n - 1, grid[n - 1].find("."))
	visited = [[False for _ in range(m)] for _ in range(n)]
	graph = construct_graph(grid, points_of_interest(grid, start, end), DIR1)

	def dfs(pt):
		if pt == end:
			return 0
		res = -float("inf")
		visited[pt[0]][pt[1]] = True 
		for npt, val in graph[pt].items():
			if not visited[npt[0]][npt[1]]:
				res = max(res, val + dfs(npt))

		visited[pt[0]][pt[1]] = False
		return res
	return dfs(start)

def part2():
	grid = []
	with open("input.txt", "r") as fp:
		grid = fp.read().strip().splitlines()
	n = len(grid)
	m = len(grid[0])
	start = (0, grid[0].find("."))
	end = (n - 1, grid[n - 1].find("."))
	visited = [[False for _ in range(m)] for _ in range(n)]
	graph = construct_graph(grid, points_of_interest(grid, start, end), DIR2)

	def dfs(pt):
		if pt == end:
			return 0
		res = -float("inf")
		visited[pt[0]][pt[1]] = True 
		for npt, val in graph[pt].items():
			if not visited[npt[0]][npt[1]]:
				res = max(res, val + dfs(npt))

		visited[pt[0]][pt[1]] = False
		return res
	return dfs(start)

if __name__ == "__main__":
	print(part1())
	print(part2())
