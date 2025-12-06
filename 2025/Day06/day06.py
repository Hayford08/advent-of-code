# Day 6: https://adventofcode.com/2025/day/6

from functools import reduce
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
        return fp.read().split("\n")


OP_MAP = {"*": lambda x, y : int(x) * int(y),
          "+": lambda x, y : int(x) + int(y)}

def part1():
    """
    Solves part 1 of the puzzle
    """
    parsed_data = []
    for line in get_input():
        parsed_data.append(line.strip().split())
    parsed_data = list(zip(*parsed_data))
    res = 0
    for row in parsed_data:
        op = OP_MAP[row[-1]]
        res += reduce(op, row[:-1])
    return res


def part2():
    """
    Solves part 2 of the puzzle
    """
    raw_data = get_input()
    ops = list(raw_data.pop().strip().split())
    parsed_data = []
    for row in raw_data:
        row = list(row)
        r = len(row) - 1
        while r >= 0 and row[r] == ' ':
            row[r] = '0'
            r -= 1

        parsed_data.append(row[::-1])
    parsed_data = list(zip(*parsed_data))
    pos = 0
    res = 0
    while pos < len(parsed_data):
        nums = []
        while pos < len(parsed_data) and any(x != ' ' for x in parsed_data[pos]):
            val = 0
            for x in parsed_data[pos]:
                if x == ' ':
                    continue
                val = val * 10 + int(x)
            nums.append(val)
            pos += 1
        pos += 1
        res += reduce(OP_MAP[ops.pop()], nums)
    return res


if __name__ == "__main__":
    # print(part1())
    print(part2())