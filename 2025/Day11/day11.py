# Day 11: https://adventofcode.com/2025/day/11

from collections import defaultdict
from functools import lru_cache
import os
import sys
import re

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

END = "out"

def parse_input():
    """
    Calls get_input and parses the input
    """
    adj = defaultdict(list)
    for line in get_input():
        match = re.match(r"([a-zA-Z]+):\s*([a-zA-Z]+(?:\s+[a-zA-Z]+)*)", line.strip())
        adj[match.group(1)] += match.group(2).split()
    return adj

def part1():
    """
    Solves part 1 of the puzzle
    """
    adj = parse_input()

    @lru_cache
    def solve(u):
        if u == END:
            return 1
        res = 0
        for v in adj[u]:
            res += solve(v)
        return res

    return solve("you")

def part2():
    """
    Solves part 2 of the puzzle
    """
    adj = parse_input()
    dp = {}

    def solve(u, mask):
        if u == END:
            return mask == 3

        if (u, mask) in dp:
            return dp[(u, mask)]

        dp[(u, mask)] = 0

        res = 0
        for v in adj[u]:
            nmask = mask
            if v == "dac":
                nmask |= 1
            elif v == "fft":
                nmask |= 2
            res += solve(v, nmask)
        dp[(u, mask)] = res
        return res

    return solve("svr", 0)

if __name__ == "__main__":
    # print(part1())
    print(part2())
