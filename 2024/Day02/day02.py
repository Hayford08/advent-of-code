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
        return fp.readlines()
    
def all_increasing(values):
    for i in range(1, len(values)):
        if values[i] <= values[i-1]:
            return False
    return True

def all_decreasing(values):
    for i in range(1, len(values)):
        if values[i] >= values[i-1]:
            return False
    return True

def good(values):
    if not all_increasing(values) and not all_decreasing(values):
        return False
    for i in range(1, len(values)):
        if not (1 <= abs(values[i] - values[i-1]) <= 3):
            return False
    return True

def part1():
    ans = 0
    for line in get_input():
        values = list(map(int, line.split()))
        if good(values):
            ans += 1
    return ans

def part2():
    ans = 0
    for line in get_input():
        values = list(map(int, line.split()))
        if good(values):
            ans += 1
            continue
        n = len(values)
        for i in range(0, n):
            nvalues = values[:i] + values[i+1:]
            if good(nvalues):
                ans += 1
                break
    return ans

if __name__ == "__main__":
    # print(part1())
    print(part2())