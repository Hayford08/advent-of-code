# Day 2: https://adventofcode.com/2025/day/2


import os
import sys

sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except OSError:
    pass

MAX_REPEAT_VALUE = int(1e6)
MAX_VALUE = int(1e10)

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
        for id_range in line.strip().split(","):
            x, y = id_range.strip().split("-")
            result.append((int(x), int(y)))
    return result

def get_invalid_ids(max_num_of_repeats = 2):
    """
    Returns IDs with repeated digits with the first part <= n
    
    :param N: Description
    """
    values = set()
    for i in range(1, MAX_REPEAT_VALUE):
        s = str(i)
        for j in range(2, max_num_of_repeats + 1):
            val = int(s * j)
            if val > MAX_VALUE:
                break
            values.add(val)
    return sorted(values)
    
def part1():
    """
    Solves part 1 of the puzzle
    """
    values = get_invalid_ids()
    res = 0
    for l, r in parse_input():
        if l > r:
            continue
        for x in values:
            if x > r:
                break
            if l <= x <= r:
                res += x
    return res

def part2():
    """
    Solves part 2 of the puzzle
    """
    values = get_invalid_ids(9)
    res = 0
    for l, r in parse_input():
        if l > r:
            continue
        for x in values:
            if x > r:
                break
            if l <= x <= r:
                res += x
    return res
    

if __name__ == "__main__":
    # print(part1())
    print(part2())