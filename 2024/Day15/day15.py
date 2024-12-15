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
        return fp.read().strip().split("\n\n")


def parse_input():
    grid, moves = get_input()
    grid = [list(row) for row in grid.split("\n")]
    moves = moves.replace("\n", "")
    return grid, moves


BOX = "O"
ROBOT = "@"
WALL = "#"
SPACE = "."
LBOX = "["
RBOX = "]"
DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}
FACTOR = 100


def part1():
    grid, moves = parse_input()
    rx, ry = -1, -1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ROBOT:
                rx, ry = i, j
                break

    for m in moves:
        dx, dy = DIRS[m]
        good = True
        boxes = []
        cx, cy = rx + dx, ry + dy
        while True:
            obj = grid[cx][cy]
            if obj == WALL or obj == SPACE:
                good = obj == SPACE
                break
            elif obj == BOX:
                boxes.append((cx, cy))
                cx += dx
                cy += dy

        if not good:
            continue
        grid[rx][ry] = SPACE
        grid[rx + dx][ry + dy] = ROBOT
        for bx, by in boxes:
            grid[bx + dx][by + dy] = BOX
        rx += dx
        ry += dy
    return sum(
        FACTOR * i + j
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == BOX
    )


def part2():
    grid, moves = parse_input()
    mp = {"O": "[]", "#": "##", ".": "..", "@": "@."}
    grid = [list("".join(mp[c] for c in row)) for row in grid]
    rx, ry = -1, -1
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == ROBOT:
                rx, ry = i, j
                break
    for m in moves:
        dx, dy = DIRS[m]
        good = True
        boxes = []
        stk = [(rx, ry)]
        visited = set()
        while stk:
            cx, cy = stk.pop()
            cx += dx
            cy += dy
            if (cx, cy) in visited:
                continue
            obj = grid[cx][cy]
            if obj == WALL:
                good = False
                break
            visited.add((cx, cy))

            if obj == LBOX:
                stk.append((cx, cy))
                stk.append((cx, cy + 1))
                boxes.append((cx, cy, LBOX))
                boxes.append((cx, cy + 1, RBOX))

            elif obj == RBOX:
                stk.append((cx, cy))
                stk.append((cx, cy - 1))
                boxes.append((cx, cy, RBOX))
                boxes.append((cx, cy - 1, LBOX))

        if not good:
            continue
        grid[rx][ry] = "."
        for bx, by, _ in boxes:
            grid[bx][by] = "."

        grid[rx + dx][ry + dy] = "@"
        for bx, by, box in boxes:
            grid[bx + dx][by + dy] = box
        rx += dx
        ry += dy
    return sum(
        FACTOR * i + j
        for i, row in enumerate(grid)
        for j, cell in enumerate(row)
        if cell == LBOX
    )


if __name__ == "__main__":
    # print(part1())
    print(part2())
