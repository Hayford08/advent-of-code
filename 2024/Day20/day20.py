from collections import Counter, deque, defaultdict
import heapq
import os
import sys
import math

sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except:
    pass


def get_input():
    with open("input.txt", "r") as fp:
        return fp.read().strip().split("\n")


def parse_input():
    grid = [list(line) for line in get_input()]
    start = None
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "S":
                start = (i, j)
                break
    return grid, start


DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def bfs(grid, sx, sy):
    n = len(grid)
    m = len(grid[0])
    q = deque([(sx, sy, 0)])
    dist = [[-1] * m for _ in range(n)]
    dist[sx][sy] = 0
    while q:
        x, y, d = q.popleft()
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < n
                and 0 <= ny < m
                and dist[nx][ny] == -1
                and grid[nx][ny] != "#"
            ):
                dist[nx][ny] = d + 1
                if grid[nx][ny] == "E":
                    return d + 1, dist
                q.append((nx, ny, d + 1))
    return -1, dist


def part1():
    grid, start = parse_input()
    _, dist = bfs(grid, start[0], start[1])
    skip = [(-1, 1), (0, 2), (1, 1), (2, 0)]
    res = 0
    n, m = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "#":
                continue
            for dx, dy in skip:
                ni, nj = i + dx, j + dy
                if (
                    0 <= ni < n
                    and 0 <= nj < m
                    and grid[ni][nj] != "#"
                    and abs(dist[i][j] - dist[ni][nj]) >= 102
                ):
                    res += 1

    return res

def part2():
    grid, start = parse_input()
    _, dist = bfs(grid, start[0], start[1])
    res = 0
    n, m = len(grid), len(grid[0])
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == "#":
                continue
            for radius in range(2, 21):
                for dx in range(radius + 1):
                    dy = radius - dx
                    for ni, nj in set([(i + dx, j + dy), (i + dx, j - dy), (i - dx, j + dy), (i - dx, j - dy)]):
                        if (
                            0 <= ni < n
                            and 0 <= nj < m
                            and grid[ni][nj] != "#"
                            and dist[i][j] - dist[ni][nj] >= 100 + radius
                        ):
                            res += 1
    return res

if __name__ == "__main__":
    # print(part1())
    print(part2())
