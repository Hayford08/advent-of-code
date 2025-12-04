# Day 3: https://adventofcode.com/2025/day/3

from functools import lru_cache
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
        result.append([int(x) for x in list(line.strip())])
    return result

def part1():
    """
    Solves part 1 of the puzzle
    """
    res = 0
    for bank in parse_input():
        mx = 0
        val = 0
        for d in bank:
            val = max(val, mx * 10 + d)
            mx = max(mx, d)
        res += val
    return res

def part2():
    """
    Solves part 2 of the puzzle
    """
    curr_values = []
    pow10 = [10 ** i for i in range(12)]

    @lru_cache
    def solve(pos, pw):
        if pos == len(curr_values) or pw == 12:
            return 0

        op1 = solve(pos + 1, pw)
        op2 = curr_values[pos] * pow10[pw] + solve(pos + 1, pw + 1)
        return max(op1, op2)

    ans = 0
    for bank in parse_input():
        curr_values = bank[::-1]
        ans += solve(0, 0)
        solve.cache_clear()
    return ans


if __name__ == "__main__":
    # print(part1())
    print(part2())