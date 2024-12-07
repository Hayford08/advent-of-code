import os

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except:
    pass

def get_input():
    with open("input.txt", "r") as fp:
        return fp.readlines()
    
def parse_input():
    result = []
    for line in get_input():
        target, rest = line.strip().split(":")
        rest = rest.strip().split(" ")
        result.append((int(target), [int(x) for x in rest]))
    return result

def solve1(data):
    dp = {}
    target, res = data
    n = len(res)
    def helper(idx, val):
        if idx == n:
            return val == target
        
        if val > target:
            return False
        
        if (idx, val) in dp:
            return dp[(idx, val)]
        if helper(idx + 1, val + res[idx]):
            dp[(idx, val)] = True
            return True
        if helper(idx + 1, val * res[idx]):
            dp[(idx, val)] = True
            return True
        dp[(idx, val)] = False
        return False
    return helper(1, res[0])

def part1():
    data = parse_input()
    ans = 0
    for d in data:
        if solve1(d):
            ans += d[0]
    return ans

def solve2(data):
    dp = {}
    target, rest = data
    n = len(rest)

    def helper(idx, val):
        if idx == n:
            return val == target

        if val > target:
            return False

        if (idx, val) in dp:
            return dp[(idx, val)]
        
        if helper(idx + 1, val + rest[idx]):
            dp[(idx, val)] = True
            return True
        if helper(idx + 1, val * rest[idx]):
            dp[(idx, val)] = True
            return True
        
        nval = int(str(val) + str(rest[idx]))
        if helper(idx + 1, nval):
            dp[(idx, val)] = True
            return True
        dp[(idx, val)] = False
        return False
        
    return helper(1, rest[0])

def part2():
    data = parse_input()
    ans = 0
    for d in data:
        if solve2(d):
            ans += d[0]
    return ans

if __name__ == "__main__":
    print(part1())
    print(part2())