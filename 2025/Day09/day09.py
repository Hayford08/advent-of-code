"""Day 9: https://adventofcode.com/2025/day/9"""

from collections import deque
import os
import sys

sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except OSError:
    pass

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

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
        result.append(tuple(map(int, line.strip().split(","))))
    return result

def part1():
    """
    Solves part 1 of the puzzle
    """
    data = parse_input()
    n = len(data)
    ans = 0
    for i, (x1, y1) in enumerate(data):
        for j in range(i + 1, n):
            x2, y2 = data[j]
            dx, dy = abs(x2 - x1) + 1, abs(y2 - y1) + 1
            ans = max(ans, dx * dy)
    return ans

def part2():
    """
    Solves part 2 of the puzzle
    """
    data = parse_input()
    x_points = sorted(set(x for x, _ in data))
    y_points = sorted(set(y for _, y in data))

    def compress(points):
        coord = {points[0] : 1}
        pt = 1
        for pv, curr in zip(points, points[1:]):
            if pv + 1 == curr:
                pt += 1
            else:
                pt += 2
            coord[curr] = pt
        return coord, pt + 1

    coord_x, n = compress(x_points)
    coord_y, m = compress(y_points)

    ## Extra padding around the grid
    n += 1
    m += 1

    grid = [[0 for _ in range(m)] for _ in range(n)]

    ## mark the borders
    sz = len(data)
    for i, (x1, y1) in enumerate(data):
        x1, y1 = coord_x[x1], coord_y[y1]
        x2, y2 = data[(i + 1) % sz]
        x2, y2 = coord_x[x2], coord_y[y2]
        if x1 == x2:
            for pt in range(min(y1, y2), max(y1, y2) + 1):
                grid[x1][pt] = 1

        if y1 == y2:
            for pt in range(min(x1, x2), max(x1, x2) + 1):
                grid[pt][y1] = 1

    ## Flood fill the outside of the grid
    visited = [[False for _ in range(m)] for _ in range(n)]
    visited[0][0] = True
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        for dx, dy in DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 0:
                visited[nx][ny] = True
                queue.append((nx, ny))

    ## Everything else not outside is inside
    for i, row in enumerate(grid):
        for j in range(m):
            if not visited[i][j]:
                row[j] = 1

    ## compute 2D prefix
    for i in range(n):
        for j in range(m):
            top = grid[i - 1][j] if i > 0 else 0
            left = grid[i][j - 1] if j > 0 else 0
            diag = grid[i - 1][j - 1] if i > 0 and j > 0 else 0
            grid[i][j] += top + left - diag

    def good_rectangle(x1, y1, x2, y2):
        """
        Determines if rectangle with diagonal corners (x1, y1) and (x2, y2)
        has all red and green tiles
        """
        x1, y1 = coord_x[x1], coord_y[y1]
        x2, y2 = coord_x[x2], coord_y[y2]

        mn_x = min(x1, x2)
        mx_x = max(x1, x2)
        mn_y = min(y1, y2)
        mx_y = max(y1, y2)

        expected_area = (mx_y - mn_y + 1) * (mx_x - mn_x + 1)
        actual_area = grid[mx_x][mx_y]
        if mn_x > 0:
            actual_area -= grid[mn_x - 1][mx_y]
        if mn_y > 0:
            actual_area -= grid[mx_x][mn_y - 1]
        if mn_x > 0 and mn_y > 0:
            actual_area += grid[mn_x - 1][mn_y - 1]
        return expected_area == actual_area

    res = 0
    for i, (x1, y1) in enumerate(data):
        for j in range(i + 1, sz):
            x2, y2 = data[j]
            if good_rectangle(x1, y1, x2, y2):
                res = max(res, (1 + abs(x1 - x2)) * (1 + abs(y1 - y2)))
    return res

if __name__ == "__main__":
    # print(part1())
    print(part2())
