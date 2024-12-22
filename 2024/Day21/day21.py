from collections import deque
import os
import sys
from itertools import product
from functools import cache

sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except:
    pass

def get_input():
    with open("input.txt", "r") as fp:
        return fp.read().strip().split("\n")

NUMERIC_KEYPAD = [['7', '8', '9'],
                  ['4', '5', '6'],
                  ['1', '2', '3'],
                  ['-1', '0', 'A']]

DIRECTIONAL_KEYPAD = [['-1', '^', 'A'],
                      ['<', 'v', '>']]

MAP = [('^', (-1, 0)), ('v', (1, 0)), ('<', (0, -1)), ('>', (0, 1))]

def shortest_paths(start, end, keypad):
    if start == end:
        return ["A"]
    queue = deque([(start, "")])
    n, m = len(keypad), len(keypad[0])
    dist = [[float("inf") for _ in range(m)] for _ in range(n)]
    dist[start[0]][start[1]] = 0
    paths = [[None for _ in range(m)] for _ in range(n)]
    while queue:
        (x, y), path = queue.popleft()
        for direction, (dx, dy) in MAP:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < n and 0 <= ny < m) or keypad[nx][ny] == "-1":
                continue
            if len(path) + 1 < dist[nx][ny]:
                dist[nx][ny] = len(path) + 1
                paths[nx][ny] = [path + direction]
                queue.append(((nx, ny), path + direction))
            elif len(path) + 1 == dist[nx][ny]:
                paths[nx][ny].append(path + direction)
                queue.append(((nx, ny), path + direction))
    ways = paths[end[0]][end[1]]
    return [way + "A" for way in ways]

def get_paths(keypad):
    positions = {}
    for i, row in enumerate(keypad):
        for j, value in enumerate(row):
            if value == "-1":
               continue
            positions[value] = (i, j)

    distance = {}
    for x, src in positions.items():
        for y, desc in positions.items():
            distance[(x, y)] = shortest_paths(src, desc, keypad)
    return distance

def solve(target, keypad):
    distance = get_paths(keypad)
    return list("".join(x) for x in product(*[distance[(x, y)] for x, y in zip("A" + target, target)]))

def part1():
    codes = get_input()

    result = 0
    for code in codes:
        robot1 = solve(code, NUMERIC_KEYPAD)
        curr = robot1
        for _ in range(2):
            nxt = []
            for path in curr:
                nxt.extend(solve(path, DIRECTIONAL_KEYPAD))
            mn = min(len(path) for path in nxt)
            curr = [path for path in nxt if len(path) == mn]
        value = int(code[:-1])
        result += value * len(curr[0])
    return result

def part2():
    codes = get_input()
    directional = get_paths(DIRECTIONAL_KEYPAD)
    mp = {key : len(value[0]) for key, value in directional.items()}

    @cache
    def compute(start, end, depth):
        if depth == 1:
            return mp[(start, end)]
        mn = float("inf")
        for path in directional[(start, end)]:
            curr = 0
            for a, b in zip("A" + path, path):
                curr += compute(a, b, depth - 1)
            mn = min(mn, curr)
        return mn
    
    result = 0
    for code in codes:
        robot1 = solve(code, NUMERIC_KEYPAD)
        value = int(code[:-1])
        mn = float("inf")
        for path in robot1:
            curr = 0
            for a, b in zip("A" + path, path):
                curr += compute(a, b, 25)
            mn = min(mn, curr)
        result += value * mn
    return result

if __name__ == "__main__":
    # print(part1())
    print(part2())