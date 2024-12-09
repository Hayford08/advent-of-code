from collections import Counter, deque, defaultdict
from sortedcontainers import SortedList
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
    data = get_input()[0].strip()
    data = list(map(int, list(data)))
    return data

def sum_range(l, r):
    res = (r * (r + 1)) // 2 - ((l - 1) * l) // 2
    return res

def compute_checksum(values):
    ans = 0
    for px, py, v_id in values:
        ans += v_id * sum_range(px, py)
    return ans

def part1():
    data = parse_input()
    pos = 0
    values = SortedList([])
    spaces = []
    v_id = 0
    for i, val in enumerate(data):
        if val == 0:
            continue
        if i % 2 == 0:
            values.add((pos, pos + val - 1, v_id))
            v_id += 1
        else:
            spaces.append((pos, pos + val - 1))
        pos += val
    for space in spaces:
        start, end = space
        while start <= end:
            num_spaces = end - start + 1
            px, py, v_id = values[-1]
            if (start > py):
                break
            values.pop()
            count = py - px + 1
            take = min(num_spaces, count)
            values.add((start, start + take - 1, v_id))
            if take < count:
                values.add((px, py - take, v_id))
            start += take
    return compute_checksum(values)

def part2():
    data = parse_input()
    values, spaces = [], SortedList([])
    pos = 0
    v_id = 0
    for i, size in enumerate(data):
        if size == 0:
            continue
        if i % 2 == 0:
            values.append((pos, pos + size - 1, v_id))
            v_id += 1
        else:
            spaces.add((pos, pos + size - 1, size))
        pos += size
    
    nvalues = []
    for px, py, v_id in values[::-1]:
        size = py - px + 1
        found = False
        for space in spaces:
            start, end, space_size = space
            if start > py:
                break
            if size <= space_size:
                spaces.remove(space)
                space_size -= size
                if space_size > 0:
                    spaces.add((start + size, end, space_size))
                nvalues.append((start, start + size - 1, v_id))
                found = True
                break
        if not found:
            nvalues.append((px, py, v_id))
    return compute_checksum(nvalues)


if __name__ == "__main__":
    # print(part1())
    print(part2())
