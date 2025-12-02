# Day 1: https://adventofcode.com/2025/day/1

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
    result = []
    for line in get_input():
        line = line.strip()
        if line[0] == 'L':
            result.append(-int(line[1:]))
        else:
            result.append(int(line[1:]))
    return result

def part1():
    """
    Solves part 1 of the puzzle
    """
    start = 50
    cnt = 0
    for x in parse_input():
        start = (start + x) % 100
        if start == 0:
            cnt += 1
    return cnt

def part2():
    """
    Solves part 2 of the puzzle
    """
    start = 50
    cnt = 0
    for x in parse_input():
        q, r = divmod(abs(x), 100)
        cnt += q
        x = r if x >= 0 else -r
        pv = start
        start += x
        if (pv != 100 and start >= 100) or (pv != 0 and start <= 0):
            cnt += 1
        start %= 100

    return cnt


if __name__ == "__main__":
    # print(part1())
    print(part2())
