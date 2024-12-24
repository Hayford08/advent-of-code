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
    start, system = get_input()
    values = defaultdict(int)
    for line in start.split("\n"):
        key, value = line.split(": ")
        values[key] = int(value)
    
    rules = []
    for line in system.split("\n"):
        line  = line.split(" -> ")
        rules.append((*line[0].split(" "), line[1]))
    return values, rules

mp = {
    "AND": lambda a, b: a & b,
    "OR": lambda a, b: a | b,
    "XOR": lambda a, b: a ^ b,
}

def simulate(values, rules):
    graph = defaultdict(list)
    todo = {}
    degree = defaultdict(int)
    for rule in rules:
        a, op, b, c = rule
        graph[a].append(c)
        graph[b].append(c)
        todo[c] = (a, op, b)
        degree[c] += 2
    
    q = deque([k for k in values])
    while q:
        u = q.popleft()
        for v in graph[u]:
            degree[v] -= 1
            if degree[v] == 0:
                a, op, b = todo[v]
                values[v] = mp[op](values[a], values[b])
                q.append(v)
    return values

def bin_value(values, x):
    xvalues = sorted([(k, v) for k, v in values.items() if k.startswith(x)], reverse=True)
    res = 0
    for _, v in xvalues:
        res = res * 2 + v
    return res

def part1():
    values, rules = parse_input()
    simulate(values, rules)
    return bin_value(values, "z")


# inspired by https://www.youtube.com/watch?v=SU6lp6wyd3I

def part2():
    values, rules = parse_input()
    todo = {}
    for rule in rules:
        a, op, b, c = rule
        todo[c] = (a, op, b)

    def make_wire(wire, num):
        return f"{wire}{num:02d}"
    
    def verity_current_z(wire, num):
        # print("Verifying z:", wire, num)
        if wire not in todo:
            return False
        a, op, b = todo[wire]
        if op != "XOR":
            return False
        if num == 0:
            return sorted([a, b]) == ["x00", "y00"]
        # Z = X ^ Y ^ C
        # C = X && Y || X && C || Y && C
        return verify_intermediate(a, num) and verify_carry_bit(b, num) or \
               verify_intermediate(b, num) and verify_carry_bit(a, num)
    
    def verify_intermediate(wire, num):
        # print("Verifying intermediate", wire, num)
        if wire not in todo:
            return False
        a, op, b = todo[wire]
        if op != "XOR":
            return False
        return sorted([a, b]) == [make_wire("x", num), make_wire("y", num)]
    
    def verify_carry_bit(wire, num):
        # print("Verifying carry bit", wire, num)
        if wire not in todo:
            return False
        a, op, b = todo[wire]
        if num == 1:
            return op == "AND" and sorted([a, b]) == ["x00", "y00"]
        return op == "OR" and (verify_direct_carry(a, num - 1) and verify_recarry(b, num - 1) or \
                               verify_direct_carry(b, num - 1) and verify_recarry(a, num - 1))
    
    def verify_direct_carry(wire, num):
        # print("Verifying direct carry", wire, num)
        if wire not in todo:
            return False
        a, op, b = todo[wire]
        return op == "AND" and sorted([a, b]) == [make_wire("x", num), make_wire("y", num)]

    def verify_recarry(wire, num):
        # print("Verifying recarry", wire, num)
        if wire not in todo:
            return False
        a, op, b = todo[wire]
        return op == "AND" and (verify_intermediate(a, num) and verify_carry_bit(b, num) or \
                                verify_intermediate(b, num) and verify_carry_bit(a, num))
        
    def verify(num):
        return verity_current_z(make_wire("z", num), num)
    
    def progress():
        num = 0
        while verify(num):
            num += 1
        return num
    
    swaps = []
    for _ in range(4):
        base = progress()
        for x, xval in todo.items():
            found = False
            for y, yval in todo.items():
                if x == y: continue
                todo[x], todo[y] = yval, xval
                if progress() > base:
                    swaps += [x, y]
                    found = True
                    break
                todo[x], todo[y] = xval, yval
            if found:
                break
    return ",".join(sorted(swaps))


if __name__ == "__main__":
    # print(part1())
    print(part2())