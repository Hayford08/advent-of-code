from collections import Counter, deque, defaultdict
import os
import re
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
        return fp.readlines()

XMAS = "XMAS"
DIAGS = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
HORIZONTAL = [(0, 1), (0, -1)]
VERTICAL = [(1, 0), (-1, 0)]
DIRS = HORIZONTAL + VERTICAL + DIAGS

def part1():
    ans = 0
    grid = []
    for line in get_input():
        grid.append(list(line.strip()))
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            for dx, dy in DIRS:
                x, y = i, j
                cnt = 0
                for k in range(4):
                    if x < 0 or x >= n or y < 0 or y >= m:
                        break
                    if grid[x][y] == XMAS[k]:
                        cnt += 1
                    x += dx
                    y += dy
                if cnt == 4:
                    ans += 1
    return ans

def rotate(grid):
    n = len(grid)
    m = len(grid[0])
    new_grid = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(grid[j][m - i - 1])
        new_grid.append(row)
    return new_grid

def check(grid, target):
    for i in range(3):
        for j in range(3):
            if target[i][j] == ".":
                continue
            if target[i][j] != grid[i][j]:
                return False
    return True

def part2():
    ans = 0
    target = ["M.S", ".A.", "M.S"]
    grid = []
    for line in get_input():
        grid.append(list(line.strip()))
    
    n = len(grid)
    m = len(grid[0])
    for i in range(n - 2):
        for j in range(m - 2):
            curr = []
            for dx in range(3):
                row = []
                for dy in range(3):
                    row.append(grid[i + dx][j + dy])
                curr.append(row)
            for _ in range(4):
                if check(curr, target):
                    ans += 1
                    break
                curr = rotate(curr)
            
    return ans

if __name__ == "__main__":
    print(part1())
    print(part2())