from collections import Counter, deque, defaultdict
import os
import sys
import math
import heapq

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
    result = [list(row) for row in get_input()]
    return result

DIRS = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def part1():
    data = parse_input()
    x, y = -1, -1
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == 'S':
                x, y = i, j
                break
    n = len(data)
    m = len(data[0])
    dp = [[[float('inf') for _ in range(4)] for _ in range(m)] for _ in range(n)]
    dp[x][y][0] = 0
    min_heap = [(0, x, y, 0)]
    while min_heap:
        cost, x, y, d = heapq.heappop(min_heap)
        if dp[x][y][d] != cost:
            continue
        if data[x][y] == 'E':
            return cost
        nx, ny = x + DIRS[d][0], y + DIRS[d][1]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != '#':
            if cost + 1 < dp[nx][ny][d]:
                dp[nx][ny][d] = cost + 1
                heapq.heappush(min_heap, (cost + 1, nx, ny, d))

        for delta in [-1, 1]:
            nd = (d + delta) % 4
            if cost + 1000 < dp[x][y][nd]:
                dp[x][y][nd] = cost + 1000
                heapq.heappush(min_heap, (cost + 1000, x, y, nd))
    return -1

def part2():
    data = parse_input()
    x, y = -1, -1
    for i, row in enumerate(data):
        for j, char in enumerate(row):
            if char == 'S':
                x, y = i, j
                break

    n = len(data)
    m = len(data[0])
    dp = [[[float('inf') for _ in range(4)] for _ in range(m)] for _ in range(n)]
    parent = defaultdict(list)
    seen = set()
    path = set()
    def get_path(curr):
        if curr in seen:
            return
        seen.add(curr)
        path.add((curr[0], curr[1]))
        for p in parent[curr]:
            get_path(p)

    dp[x][y][0] = 0
    min_heap = [(0, x, y, 0)]
    while min_heap:
        cost, x, y, d = heapq.heappop(min_heap)
        if dp[x][y][d] != cost:
            continue
        
        if data[x][y] == 'E':
            get_path((x, y, d))
            return len(path)
        
        nx, ny = x + DIRS[d][0], y + DIRS[d][1]
        if 0 <= nx < n and 0 <= ny < m and data[nx][ny] != '#':
            if cost + 1 < dp[nx][ny][d]:
                parent[(nx, ny, d)] = [(x, y, d)]
                dp[nx][ny][d] = cost + 1
                heapq.heappush(min_heap, (cost + 1, nx, ny, d))
            elif cost + 1 == dp[nx][ny][d]:
                parent[(nx, ny, d)].append((x, y, d))

        for delta in [-1, 1]:
            nd = (d + delta) % 4
            if cost + 1000 < dp[x][y][nd]:
                parent[(x, y, nd)] = [(x, y, d)]
                dp[x][y][nd] = cost + 1000
                heapq.heappush(min_heap, (cost + 1000, x, y, nd))
            elif cost + 1000 == dp[x][y][nd]:
                parent[(x, y, nd)].append((x, y, d))
    return -1

if __name__ == "__main__":
    print(part1())
    print(part2())