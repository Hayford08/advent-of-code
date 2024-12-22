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
        return fp.read().strip().split("\n")


def parse_input():
    return list(map(int, get_input()))


MOD = 16777216


def mix(x, val):
    return x ^ val


def prune(x):
    return x % MOD


def generate(x):
    values = [x % 10]
    for _ in range(2000):
        x = mix(x, x * 64)
        x = prune(x)
        x = mix(x, x // 32)
        x = prune(x)
        x = mix(x, x * 2048)
        x = prune(x)
        values.append(x % 10)
    return x, values


def part1():
    data = parse_input()
    res = 0
    for x in data:
        res += generate(x)[0]
    return res


def part2():
    data = parse_input()
    pattern = defaultdict(int)
    for x in data:
        _, values = generate(x)
        queue = deque([])
        seen = set()
        for i, v in enumerate(values):
            if i == 0:
                continue
            queue.append(v - (values[i - 1]))
            if len(queue) == 4:
                tup = tuple(queue)
                if tup not in seen:
                    pattern[tup] += v
                    seen.add(tup)
                queue.popleft()
    return max(pattern.values())


if __name__ == "__main__":
    # print(part1())
    print(part2())
