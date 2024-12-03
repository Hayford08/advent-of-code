from collections import Counter, deque, defaultdict
import re
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
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
    for line in get_input():
        matches = re.findall(pattern, line)
        for match in matches:
            ans += int(match[0]) * int(match[1])
    return ans

def part2():
    ans = 0
    pattern = r"(?P<mul>mul\((\d{1,3}),\s*(\d{1,3})\))|(?P<do>do\(\))|(?P<dont>don't\(\))"
    flag = True
    for line in get_input():
        matches = re.finditer(pattern, line)
        for match in matches:
            if match.group("mul") and flag:
                values = match.group("mul")[:-1]
                values = values[4:].split(",")
                ans += int(values[0]) * int(values[1])
            elif match.group("do"):
                flag = True
            elif match.group("dont"):
                flag = False
            
    return ans

if __name__ == "__main__":
    # print(part1())
    print(part2())