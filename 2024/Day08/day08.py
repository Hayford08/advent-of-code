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
    grid = []
    for line in get_input():
        line = list(line.strip())
        grid.append(line)
    graph = defaultdict(list)
    n = len(grid)
    m = len(grid[0])
    for i in range(n):
        for j in range(m):
            ch = grid[i][j]
            if ch.isalnum():
                graph[ch].append((i, j))
    return graph, (n, m)

def get_antinodes(pt1, pt2):
    x1, y1 = pt1
    x2, y2 = pt2
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    if y1 > y2:
        return (x1 - dx, y1 + dy), (x2 + dx, y2 - dy)
    return (x1 - dx, y1 - dy), (x2 + dx, y2 + dy)
    

def part1():
    graph, dims = parse_input()
    n, m = dims
    st = set()
    for _, v in graph.items():
        sz = len(v)
        for i in range(sz):
            for j in range(i + 1, sz):
                for x, y in get_antinodes(v[i], v[j]):
                    if 0 <= x < n and 0 <= y < m:
                        st.add((x, y))
    return len(st)

def get_points(pt, dx, dy, n, m):
    x, y = pt
    x += dx
    y += dy
    res = []
    while 0 <= x < n and 0 <= y < m:
        res.append((x, y))
        x += dx
        y += dy
    return res


def part2():
    graph, dims = parse_input()
    n, m = dims
    st = set()
    for _, v in graph.items():
        sz = len(v)
        for i in range(sz):
            for j in range(i + 1, sz):
                x1, y1 = v[i]
                x2, y2 = v[j]
                dx = abs(x1 - x2)
                dy = abs(y1 - y2)
                cnt = 0
                if y1 > y2:
                    for pt in get_points((x1, y1), -dx, dy, n, m):
                        st.add(pt)
                        cnt += 1
                    for pt in get_points((x2, y2), dx, -dy, n, m):
                        st.add(pt)
                        cnt += 1
                else:
                    for pt in get_points((x1, y1), -dx, -dy, n, m):
                        st.add(pt)
                        cnt += 1
                    for pt in get_points((x2, y2), dx, dy, n, m):
                        st.add(pt)
                        cnt += 1
                st.add((x1, y1))
                st.add((x2, y2))
    return len(st)

if __name__ == "__main__":
    # print(part1())
    print(part2())