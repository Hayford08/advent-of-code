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
    
def get_graph(section):
    graph = defaultdict(set)
    for line in section.split('\n'):
        u, v = line.split('|')
        graph[u].add(v)
    return graph

def good(graph, nodes):
    n = len(nodes)
    for i in range(n):
        u = nodes[i]
        for j in range(i + 1, n):
            v = nodes[j]
            if u in graph[v]:
                return False
    return True

def part1():
    ans = 0
    section1, section2 = get_input()
    graph = get_graph(section1)
    for line in section2.split('\n'):
        nodes = line.strip().split(',')
        if good(graph, nodes):
            ans += int(nodes[len(nodes) // 2])
    return ans

def part2():
    ans = 0
    section1, section2 = get_input()
    graph = get_graph(section1)

    def cmp(u, v):
        if u in graph[v]:
            return -1
        if v in graph[u]:
            return 1
        return 0

    for line in section2.split('\n'):
        nodes = line.strip().split(',')
        if good(graph, nodes):
            continue
        order = sorted(nodes, key=cmp_to_key(cmp))
        ans += int(order[len(nodes) // 2])
    return ans

if __name__ == "__main__":
    # print(part1())
    print(part2())