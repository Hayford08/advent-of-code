# Day 4: https://adventofcode.com/2025/day/4

from collections import deque
import os
import sys
sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except OSError:
    pass

PAPER_ROLL = "@"
DIRECTIONS = [(-1, -1), (-1, 0), (-1, 1),
              (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]

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
    result = []
    for line in get_input():
        result.append(list(line.strip()))
    return result

def part1():
    """
    Solves part 1 of the puzzle
    """
    data = parse_input()
    n = len(data)
    m = len(data[0])
    res = 0
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == ".":
                continue
            cnt = 0
            for dx, dy in DIRECTIONS:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and data[ni][nj] == PAPER_ROLL:
                    cnt += 1
            if cnt < 4:
                res += 1
    return res

def part2():
    """
    Solves part 2 of the puzzle
    """
    data = parse_input()
    n, m = len(data), len(data[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    neighbors = [[0 for _ in range(m)] for _ in range(n)]
    q = deque([])
    for i, row in enumerate(data):
        for j, val in enumerate(row):
            if val == ".":
                continue
            cnt = 0
            for dx, dy in DIRECTIONS:
                ni, nj = i + dx, j + dy
                if 0 <= ni < n and 0 <= nj < m and data[ni][nj] == PAPER_ROLL:
                    cnt += 1
            neighbors[i][j] = cnt
            if cnt < 4:
                q.append((i, j))
                visited[i][j] = True

    res = 0
    while q:
        x, y = q.popleft()
        res += 1
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and data[nx][ny] == PAPER_ROLL and (not visited[nx][ny]):
                neighbors[nx][ny] -= 1
                if neighbors[nx][ny] < 4:
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return res

if __name__ == "__main__":
    # print(part1())
    print(part2())