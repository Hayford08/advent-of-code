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
    def get_lock(data):
        n = len(data)
        m = len(data[0])
        combo = []
        for j in range(m):
            cnt = 0
            while cnt < n and data[cnt][j] == "#":
                cnt += 1
            combo.append(cnt)
        return tuple(combo)

    def get_key(data):
        n = len(data)
        m = len(data[0])
        combo = []
        for j in range(m):
            cnt = 0
            pos = n - 2
            while pos >= 0 and data[pos][j] == "#":
                cnt += 1
                pos -= 1
            combo.append(cnt)
        return tuple(combo)

    locks, keys = [], []
    for section in get_input():
        section = section.split("\n")
        if section[0] == "#####":
            locks.append(get_lock(section[1:]))
        else:
            keys.append(get_key(section[1:]))
    return locks, keys


def part1():
    locks, keys = parse_input()
    result = 0
    for key in keys:
        for lock in locks:
            good = True
            for i, k in enumerate(key):
                if k + lock[i] >= 6:
                    good = False
                    break
            if good:
                result += 1
    return result


if __name__ == "__main__":
    print(part1())
