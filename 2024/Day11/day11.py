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

def parse_input():
    result = []
    for line in get_input():
        line = line.strip()
        if line:
            result.append(list(map(int, line.split())))
    return result[0]

N = 75
YEAR = 2024

def part1():
    data = parse_input()
    for _ in range(N):
        ndata = []
        for val in data:
            if val == 0:
                ndata.append(1)
            else:
                s = str(val)
                size = len(s)
                if size % 2 == 0:
                    ndata.append(int(s[:size//2]))
                    ndata.append(int(s[size//2:]))
                else:
                    ndata.append(val * YEAR)
        data = ndata
    return len(data)

def part2():
    data = parse_input()
    dp = {}

    def solve(stone, blink):
        if blink == 0:
            return 1
        if (stone, blink) in dp:
            return dp[(stone, blink)]
        ans = 0
        if stone == 0:
            ans = solve(1, blink - 1)
        else:
            s = str(stone)
            size = len(s)
            if size % 2 == 0:
                op1 = int(s[:size//2])
                op2 = int(s[size//2:])
                ans = solve(op1, blink - 1) + solve(op2, blink - 1)
            else:
                ans = solve(stone * YEAR, blink - 1)
        dp[(stone, blink)] = ans
        return ans
    
    ans = 0
    for stone in data:
        ans += solve(stone, N)
    return ans

if __name__ == "__main__":
    # print(part1())
    print(part2())