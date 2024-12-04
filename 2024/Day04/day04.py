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

def part2():
    ans = 0
    grid = []
    for line in get_input():
        grid.append(list(line.strip()))
    
    n = len(grid)
    m = len(grid[0])
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if grid[i][j] != "A":
                continue
            corners = [grid[i - 1][j - 1], grid[i - 1][j + 1], grid[i + 1][j + 1], grid[i + 1][j - 1]]
            if "".join(corners) in ["MMSS", "MSSM", "SSMM", "SMMS"]:
                ans += 1
    return ans

if __name__ == "__main__":
    print(part1())
    print(part2())