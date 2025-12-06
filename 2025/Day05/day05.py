# Day 5: https://adventofcode.com/2025/day/5

from collections import Counter, deque, defaultdict
import os
import sys
import bisect

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
        return fp.read().strip().split("\n\n")
  
def parse_input():
    """
    Calls get_input and parses the input
    """
    top, bottom = get_input()
    ranges = []
    for line in top.split("\n"):
        l, r = line.split("-")
        ranges.append((int(l), int(r)))
    ranges.sort()
    intervals = []
    i, n = 0, len(ranges)
    while i < n:
        x, y = ranges[i]
        while i < n and ranges[i][0] <= y:
            y = max(y, ranges[i][1])
            i += 1
        intervals.append((x, y))
    queries = [int(q) for q in bottom.split("\n")]
    return intervals, queries

def is_within(intervals, x):
    """
    Checks if x is within any of the sorted [l, r] ranges in intervals
    """
    l, r = 0, len(intervals) - 1
    while l <= r:
        mid = l + (r - l) // 2
        start, end = intervals[mid]
        if start <= x <= end:
            return True
        if x < start:
            r = mid - 1
        else:
            l = mid + 1
    return False

def part1():
    """
    Solves part 1 of the puzzle
    """
    intervals, queries = parse_input()
    return sum(is_within(intervals, q) for q in queries)

def part2():
    """
    Solves part 2 of the puzzle
    """
    intervals, _ = parse_input()
    res = 0
    for l, r in intervals:
        res += r - l + 1
    return res

if __name__ == "__main__":
    print(part1())
    print(part2())