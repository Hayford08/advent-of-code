from collections import Counter, deque, defaultdict
from functools import cmp_to_key
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

section1, section2 = get_input()
graph = defaultdict(set)
for line in section1.split('\n'):
    a, b = line.split('|')
    graph[a].add(b)

def cmp(u, v):
    if u in graph[v]:
        return -1
    if v in graph[u]:
        return 1
    return 0

def part1():
    ans = 0
    for nodes in section2.split('\n'):
        nodes = nodes.strip().split(',')
        order = sorted(nodes, key=cmp_to_key(cmp), reverse=True)
        if order == nodes:
            ans += int(nodes[len(nodes) // 2])
    return ans

def part2():
    ans = 0
    for nodes in section2.split('\n'):
        nodes = nodes.strip().split(',')
        order = sorted(nodes, key=cmp_to_key(cmp), reverse=True)
        if order != nodes:
            ans += int(order[len(nodes) // 2])
    return ans

if __name__ == "__main__":
    # print(part1())
    print(part2())