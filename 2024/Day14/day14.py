from collections import Counter, deque, defaultdict
import os
import sys
import re
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

N = 101
M = 103
SECONDS = 100

def parse_input():
    result = []
    for line in get_input():
        pattern = r"p=(\d+),(\d+) v=(-?\d+),(-?\d+)"
        x, y, vx, vy = map(int, re.match(pattern, line.strip()).groups())
        result.append((x, y, vx, vy))
    return result

def part1():
    robots = parse_input()
    for _ in range(SECONDS):
        nrobots = []
        for x, y, vx, vy in robots:
            nx = (x + vx) % N
            ny = (y + vy) % M
            nrobots.append((nx, ny, vx, vy))
        robots = nrobots
    quadrants = [0 for _ in range(4)]
    for x, y,_, _ in robots:
        if x < N//2 and y < M//2:
            quadrants[0] += 1
        elif x > N//2 and y < M//2:
            quadrants[1] += 1
        elif x < N//2 and y > M//2:
            quadrants[2] += 1
        elif x > N//2 and y > M//2:
            quadrants[3] += 1
    val = 1
    for x in quadrants:
        val *= x
    return val

def part2():
    robots = parse_input()

    def get_board(robots):
        board = [["." for _ in range(N)] for _ in range(M)]
        grid = ""
        for x, y, _, _ in robots:
            board[y][x] = "#"
        for row in board:
            grid += "".join(row) + "\n"
        return grid
    
    seconds = 0
    for _ in range(10000):
        nrobots = []
        for x, y, vx, vy in robots:
            nx = (x + vx) % N
            ny = (y + vy) % M
            nrobots.append((nx, ny, vx, vy))
        robots = nrobots
        grid = get_board(robots)
        seconds += 1
        if "########" in grid:
            print(grid)
            break
    return seconds

if __name__ == "__main__":
    # print(part1())
    print(part2())