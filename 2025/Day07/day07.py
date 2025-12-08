# Day 7: https://adventofcode.com/2025/day/7

from collections import deque
import os
import sys

sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except OSError:
    pass

def get_input():
    """
    Reads input file and returns list of lines
    """
    with open("input.txt", "r", encoding="utf-8") as fp:
        return fp.read().strip().split("\n")
  
def parse_input():
    """
    Calls get_input and parses the input
    """
    grid = get_input()
    sy = grid[0].find("S")
    return (sy, grid)

SPLITTER = "^"
DY = [-1, 1]

def part1():
    """
    Solves part 1 of the puzzle
    """
    sy, grid = parse_input()
    n, m = len(grid), len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][sy] = True
    queue = deque([(0, sy)])
    res = 0
    while queue:
        x, y = queue.pop()
        nx = x + 1
        if nx < n and not visited[nx][y]:
            if grid[nx][y] != SPLITTER:
                visited[nx][y] = True
                queue.append((nx, y))
                continue

            res += 1
            for dy in DY:
                ny = y + dy
                if 0 <= ny < m and not visited[nx][ny]:
                    queue.append((nx, ny))
                    visited[nx][ny] = True
    return res

def part2():
    """
    Solves part 2 of the puzzle
    """
    sy, grid = parse_input()
    n, m = len(grid), len(grid[0])
    count = [[0 for _ in range(m)] for _ in range(n)]
    count[0][sy] = 1
    queue = deque([(0, sy)])
    while queue:
        next_level = set()
        for x, y in queue:
            nx = x + 1
            if nx >= n:
                continue
            if grid[nx][y] != SPLITTER:
                count[nx][y] += count[x][y]
                next_level.add((nx, y))
            else:
                for dy in DY:
                    ny = y + dy
                    if 0 <= ny < m:
                        count[nx][ny] += count[x][y]
                        next_level.add((nx, ny))
        queue = deque(next_level)
    return sum(count[-1])

if __name__ == "__main__":
    # print(part1())
    print(part2())