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
        return fp.read().strip().split("\n")


N = 71
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def steps_to_target(grid):
    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[0][0] = True
    q = deque([(0, 0)])
    steps = 0
    while q:
        steps += 1
        for _ in range(len(q)):
            x, y = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < N
                    and 0 <= ny < N
                    and not visited[nx][ny]
                    and grid[nx][ny] == "."
                ):
                    if nx == N - 1 and ny == N - 1:
                        return steps
                    visited[nx][ny] = True
                    q.append((nx, ny))
    return -1


def part1():
    grid = [["." for _ in range(N)] for _ in range(N)]
    input_data = get_input()
    mx = min(len(input_data), 1024)
    for line in input_data[:mx]:
        x, y = map(int, line.strip().split(","))
        grid[y][x] = "#"
    return steps_to_target(grid)


def part2():
    data = get_input()
    blocks = []
    for line in data:
        y, x = map(int, line.strip().split(","))
        blocks.append((y, x))

    def good(index):
        grid = [["." for _ in range(N)] for _ in range(N)]
        for y, x in blocks[: index + 1]:
            grid[y][x] = "#"
        return steps_to_target(grid) != -1

    l, r = 0, len(data) - 1
    ans = r
    while l <= r:
        mid = l + (r - l) // 2
        if not good(mid):
            ans = mid
            r = mid - 1
        else:
            l = mid + 1
    y, x = blocks[ans]
    return f"{y},{x}"


if __name__ == "__main__":
    # print(part1())
    print(part2())
