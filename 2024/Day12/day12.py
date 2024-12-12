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
    
def parse_input():
    result = []
    for line in get_input():
        result.append(list(line.strip()))
    return result

DIRS = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def part1():
    grid = parse_input()
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x, y, region):
        visited[x][y] = True
        area, perimeter = 1, 0
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != region:
                perimeter += 1
                continue
            
            if visited[nx][ny]:
                continue

            a, p = dfs(nx, ny, region)
            area += a
            perimeter += p
            
        return area, perimeter
    result = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                a, p = dfs(i, j, grid[i][j])
                result += a * p
    return result

def part2():
    grid = parse_input()
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]

    def dfs(x, y, region):
        visited[x][y] = True 
        area = 1
        boundary = set()
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m) or grid[nx][ny] != region:
                boundary.add((x, y, dx, dy))
                continue
            if visited[nx][ny]:
                continue
            a, b = dfs(nx, ny, region)
            area += a
            boundary |= b
        return area, boundary
    
    result = 0
    for i in range(n):
        for j in range(m):
            if not visited[i][j]:
                area, boundary = dfs(i, j, grid[i][j])
                sides = 0
                for x, y, dx, dy in sorted(boundary):
                    if dx != 0 and (x, y - 1, dx, dy) not in boundary:
                        sides += 1
                    if dy != 0 and (x - 1, y, dx, dy) not in boundary:
                        sides += 1
                result += area * sides
    return result


if __name__ == "__main__":
    # print(part1())
    print(part2())