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

def get_max_clique(graph):
    max_clique = set()

    def bron_kerbosch(curr, potential, processed):
        if not potential and not processed:
            nonlocal max_clique
            if len(curr) > len(max_clique):
                max_clique = curr
            return

        parr = list(potential)
        while parr:
            u = parr.pop()
            ncurr = curr | {u}
            npotential = potential & graph[u]
            nprocessed = processed & graph[u]

            bron_kerbosch(ncurr, npotential, nprocessed)
            potential.remove(u)
            processed.add(u)
    
    bron_kerbosch(set(), set(graph.keys()), set())
    return max_clique


def part2():
    graph = parse_input()
    result = get_max_clique(graph)
    return ",".join(sorted(result))


if __name__ == "__main__":
    # print(part1())
    print(part2())
