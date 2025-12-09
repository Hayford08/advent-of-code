# Day 8: https://adventofcode.com/2025/day/8

from functools import reduce
import os
import sys

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
        return fp.read().strip().split("\n")
  
def parse_input():
    """
    Calls get_input and parses the input
    """
    result = []
    for line in get_input():
        result.append(tuple(map(int, line.strip().split(","))))
    return result

class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
    def find(self, a):
        if a == self.parent[a]:
            return a
        res = self.find(self.parent[a])
        self.parent[a] = res
        return res

    def merge(self, a, b):
        par_a = self.find(a)
        par_b = self.find(b)
        if par_a == par_b:
            return False
        if self.size[par_a] < self.size[par_b]:
            a, b = b, a
        
        self.size[par_a] += self.size[par_b]
        self.parent[par_b] = par_a
        return True

def part1():
    """
    Solves part 1 of the puzzle
    """
    boxes = parse_input()
    distances = []
    n = len(boxes)
    for i, (x1, y1, z1) in enumerate(boxes):
        for j in range(i + 1, n):
            x2, y2, z2 = boxes[j]
            d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((d, i, j))
    distances.sort()
    dsu = DSU(n)
    for _, u, v in distances[:1000]:
        dsu.merge(u, v)

    circuits = set()
    for i in range(n):
        root = dsu.find(i)
        circuits.add((dsu.size[root], root))

    largest = [x for x,_ in sorted(circuits, reverse=True)[:3]]
    return reduce(lambda x, y: x * y, largest)

def part2():
    """
    Solves part 2 of the puzzle
    """
    boxes = parse_input()
    distances = []
    n = len(boxes)
    for i, (x1, y1, z1) in enumerate(boxes):
        for j in range(i + 1, n):
            x2, y2, z2 = boxes[j]
            d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
            distances.append((d, i, j))
    distances.sort()
    dsu = DSU(n)
    x1, x2 = 0, 0
    for _, u, v in distances:
        if dsu.merge(u, v):
            x1, x2 = boxes[u][0], boxes[v][0]
    return x1 * x2

if __name__ == "__main__":
    # print(part1())
    print(part2())