# Day 12: https://adventofcode.com/2025/day/12

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
        data = fp.read().strip()
        index = data.rfind("\n\n")
        return data[:index], data[index + 2:]

def parse_input():
    """
    Calls get_input and parses the input
    """
    top, bottom = get_input()
    shapes = []
    for info in top.split("\n\n"):
        cnt = info.count('#')
        info = info[info.find("\n") + 1:]
        shapes.append((info.split(), cnt))

    regions = []
    for line in bottom.split("\n"):
        p1, p2 = line.split(": ")
        dim = tuple(map(int, p1.split("x")))
        amt = tuple(map(int, p2.split()))
        regions.append((dim, amt))
    return shapes, regions

def part1():
    """
    Solves part 1 of the puzzle
    """
    shapes, regions = parse_input()
    res = 0
    for (l, w), freq in regions:
        total = sum(x[1] * y for x, y in zip(shapes, freq))
        res += total <= l * w
    return res

if __name__ == "__main__":
    print(part1())
