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

def get_input():
    with open("input.txt", "r") as fp:
        return fp.readlines()

def get_grid_and_start_point():
    grid = []
    for line in get_input():
        grid.append(list(line.strip()))
    x, y = -1, -1
    n, m = len(grid), len(grid[0])
    for i in range(n):
        if x != -1:
            break
        for j in range(m):
            if grid[i][j] == '^':
                x, y = i, j
                break
    return grid, x, y

def traverse(grid, x, y):
    dx, dy = -1, 0
    n = len(grid)
    m = len(grid[0])
    while True:
        if x < 0 or x >= n or y < 0 or y >= m:
            break

        if grid[x][y] == '#':
            x -= dx
            y -= dy
            dx, dy = dy, -dx

        else:
            grid[x][y] = 'X'

        x += dx
        y += dy
    return sum([1 for row in grid for cell in row if cell == 'X'])



def part1():
    grid, x, y = get_grid_and_start_point()
    return traverse(grid, x, y)


DIRS = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def is_loop(grid, x, y, sx, sy):
    ngrid = [row[:] for row in grid]
    ngrid[x][y] = '#'
    pos = 0
    n = len(grid)
    m = len(grid[0])
    x, y = sx, sy
    visited = set()
    while True:
        if x < 0 or x >= n or y < 0 or y >= m:
            break

        if ngrid[x][y] == '#':
            x -= DIRS[pos][0]
            y -= DIRS[pos][1]
            pos = (pos + 1) % 4

        if (x, y, pos) in visited:
            return True
        
        visited.add((x, y, pos))
        ngrid[x][y] = 'X'

        x += DIRS[pos][0]
        y += DIRS[pos][1]
    return False

def part2():
    grid, x, y = get_grid_and_start_point()
    n = len(grid)
    m = len(grid[0])
    loops = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '.' and is_loop(grid, i, j, x, y):
                loops += 1
    return loops

if __name__ == "__main__":
    # print(part1())
    print(part2())