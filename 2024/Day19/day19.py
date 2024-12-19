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
    towels, designs = get_input()
    towels = towels.strip().split(",")
    towels = set([towel.strip() for towel in towels])
    designs = designs.strip().split("\n")
    return towels, designs


def solve(towels, design):
    n = len(design)
    dp = [-1 for _ in range(n)]

    def helper(index):
        if index == n:
            return 1
        if dp[index] != -1:
            return dp[index]
        res = 0
        dp[index] = 0
        curr = ""
        for i in range(index, n):
            curr += design[i]
            if curr in towels:
                res += helper(i + 1)
        dp[index] = res
        return res

    return helper(0)


def part1():
    towels, designs = parse_input()
    count = 0
    for design in designs:
        if solve(towels, design):
            count += 1
    return count


def part2():
    towels, designs = parse_input()
    count = 0
    for design in designs:
        count += solve(towels, design)
    return count


if __name__ == "__main__":
    # print(part1())
    print(part2())
