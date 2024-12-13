from collections import Counter, deque, defaultdict
import os
import sys
import re
import heapq
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


COSTA = 3
COSTB = 1
MAX_STEPS = 100
DELTA = 10000000000000

def get_x_y(text):
    pattern = "Button [AB]: X\+(\d+), Y\+(\d+)"
    match = re.match(pattern, text)
    x, y = int(match.group(1)), int(match.group(2))
    return x, y

def parse_input():
    result = []
    for line in get_input():
        data = line.split("\n")
        buttonA = get_x_y(data[0])
        buttonB = get_x_y(data[1])
        pattern = "Prize: X=(\d+), Y=(\d+)"
        match = re.match(pattern, data[2])
        prize = int(match.group(1)), int(match.group(2))
        result.append((buttonA, buttonB, prize))
    return result

def solve(info):
    buttonA, buttonB, prize = info
    x, y = prize
    cost = {(0, 0): 0}
    min_heap = [(0, 0, 0, 0, 0)] # cost, x, y, bA, bB

    while min_heap:
        curr_cost, x, y, bA, bB = heapq.heappop(min_heap)
        if x == prize[0] and y == prize[1]:
            return curr_cost 
        if curr_cost > cost[(x, y)]:
            continue
        if bA + 1 < MAX_STEPS:
            new_cost = curr_cost + COSTA
            nx, ny = x + buttonA[0], y + buttonA[1]
            if new_cost < cost.get((nx, ny), float("inf")):
                cost[(nx, ny)] = new_cost
                heapq.heappush(min_heap, (new_cost, nx, ny, bA + 1, bB))
        if bB + 1 < MAX_STEPS:
            new_cost = curr_cost + COSTB
            nx, ny = x + buttonB[0], y + buttonB[1]
            if new_cost < cost.get((nx, ny), float("inf")):
                cost[(nx, ny)] = new_cost
                heapq.heappush(min_heap, (new_cost, nx, ny, bA, bB + 1))
    return -1


def part1():
    data = parse_input()
    result = 0
    for info in data:
        val = solve(info)
        if val == -1:
            continue
        result += val
    return result

def part2():
    data = parse_input()

    def sub(arr1, arr2):
        return [x - y for x, y in zip(arr1, arr2)]
    
    def mul(arr, val):
        return [x * val for x in arr]

    def solve2(info):
        buttonA, buttonB, prize = info
        prize = (prize[0] + DELTA, prize[1] + DELTA)
        ax, ay = buttonA
        bx, by = buttonB
        px, py = prize

        eqn1 = (ax, bx, px)
        eqn2 = (ay, by, py)

        lcma = math.lcm(ax, ay)
        eqn1 = mul(eqn1, lcma // ax)
        eqn2 = mul(eqn2, lcma // ay)

        neqn = sub(eqn1, eqn2)
        if neqn[1] == 0 or neqn[2] % neqn[1] != 0:
            return -1
        bcnt = neqn[2] // neqn[1]
        num = (px - bx * bcnt) 
        if num % ax != 0:
            return -1
        acnt = num // ax
        return acnt * COSTA + bcnt * COSTB

    result = 0
    for info in data:
        val = solve2(info)
        if val == -1:
            continue
        result += val

    return result

if __name__ == "__main__":
    # print(part1())
    print(part2())