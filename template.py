# Day X: https://adventofcode.com/2025/day/X

from collections import Counter, deque, defaultdict
import os
import sys
import math

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
        pass
    return result

def part1():
    """
    Solves part 1 of the puzzle
    """
    data = parse_input()

def part2():
    """
    Solves part 2 of the puzzle
    """
    data = parse_input()

if __name__ == "__main__":
    print(part1())
    print(part2())