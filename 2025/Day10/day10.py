# Day 10: https://adventofcode.com/2025/day/10

import os
import sys

sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except OSError:
    pass
P = 10 ** 9 + 7

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
        line = line.strip()
        pos1 = line.find("]")
        diagram = line[1:pos1]
        pos2 = line.find("{")
        joltage = tuple(map(int, line[pos2 + 1:-1].split(",")))
        buttons = line[pos1 + 1:pos2].split()
        buttons = [tuple(map(int, button[1:-1].split(","))) for button in buttons]
        result.append((diagram, buttons, joltage))
    return result

def part1():
    """
    Solves part 1 of the puzzle
    """
    res = 0
    for diagram, buttons, _ in parse_input():
        n = len(diagram)
        m = len(buttons)
        presses = float("inf")
        for mask in range(1, 2 ** m):
            machine = ["."] * n
            cnt = 0
            for i in range(m):
                if not mask & (1 << i):
                    continue
                cnt += 1
                for pos in buttons[i]:
                    machine[pos] = "." if machine[pos] == "#" else "#"
            if "".join(machine) == diagram:
                presses = min(presses, cnt)
        res += presses
    return res

def part2():
    """
    Solves part 2 of the puzzle
    """
    import z3
    def presses_required(buttons, joltage):
        """
        Returns the minimum button presses required to get joltage or INF if impossible
        """
        n = len(buttons)

        # variables representing buttons
        b_vars = [z3.Int(f"b{i}") for i in range(n)]

        opt = z3.Optimize()
        # ensure that each number of presses is non-negative
        opt.add([bi >= 0 for bi in b_vars])

        for i, val in enumerate(joltage):
            possible_buttons = [b_vars[j] for j in range(n) if i in buttons[j]]
            opt.add(z3.Sum(possible_buttons) == val)

        opt.minimize(z3.Sum(b_vars))

        if opt.check() != z3.sat:
            return float("inf")

        return sum(opt.model().eval(bi).as_long() for bi in b_vars)

    res = 0
    for _, buttons, joltage in parse_input():
        res += presses_required(buttons, joltage)
    return res

if __name__ == "__main__":
    # print(part1())
    print(part2())