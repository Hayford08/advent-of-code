from collections import Counter, deque, defaultdict
import os
import sys
import math
from itertools import combinations

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
    graph = defaultdict(set)
    for line in get_input():
        u, v = line.strip().split("-")
        graph[u].add(v)
        graph[v].add(u)
    return graph


def find_triangles(graph):
    triangles = set()
    vertices = sorted(graph.keys(), key=lambda x: len(graph[x]))
    order = {v: i for i, v in enumerate(vertices)}
    for u in vertices:
        for v in graph[u]:
            if order[u] < order[v]:
                common = graph[u] & graph[v]
                for w in common:
                    if order[v] < order[w]:
                        triangles.add(tuple(sorted([u, v, w])))
    return triangles


def part1():
    graph = parse_input()
    triangles = find_triangles(graph)
    res = 0
    for triangle in triangles:
        for u in triangle:
            if u.startswith("t"):
                res += 1
                break
    return res


def part2():
    graph = parse_input()
    scc = set()

    def dfs(u, components):
        key = tuple(sorted(components))
        if key in scc:
            return

        scc.add(key)
        for v in graph[u]:
            if v in components:
                continue
            if all(v in graph[w] for w in components):
                dfs(v, {*components, v})

    for u in graph:
        dfs(u, {u})
    mx = 0
    result = None
    for sc in scc:
        if len(sc) > mx:
            mx = len(sc)
            result = sc
    return ",".join(sorted(result))


if __name__ == "__main__":
    # print(part1())
    print(part2())
