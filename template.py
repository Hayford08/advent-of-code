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

def part1():
    ans = 0
    for line in get_input():
        pass 
    return ans

def part2():
    ans = 0
    for line in get_input():
        pass
    return ans

if __name__ == "__main__":
    print(part1())
    print(part2())