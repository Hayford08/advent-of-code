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
    result = []
    for line in get_input():
        line = line.strip()
        if not line:
            continue
        result.append(list(map(int, list(line))))
    return result

DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def part1():
    data = parse_input()
    n = len(data)
    m = len(data[0])

    def get_score(px, py):
        visited = [[False for _ in range(m)] for _ in range(n)]
        q = deque([(px, py, 0)])
        visited[px][py] = True
        nines = set()
        while q:
            x, y, value = q.popleft()
            for dx, dy in DIRS:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= n or ny < 0 or ny >= m or visited[nx][ny] or data[nx][ny] != value + 1:
                    continue
                if data[nx][ny] == 9:
                    nines.add((nx, ny))
                    continue
                visited[nx][ny] = True
                q.append((nx, ny, value + 1))
        return len(nines)


    ans = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                ans += get_score(i, j)
    return ans

def part2():
    data = parse_input()
    n = len(data)
    m = len(data[0])
    dp = [[-1 for _ in range(m)] for _ in range(n)]

    def get_score(px, py):
        value = data[px][py]
        if value == 9:
            return 1
        
        if dp[px][py] != -1:
            return dp[px][py]
        
        res = 0
        for dx, dy in DIRS:
            npx, npy = px + dx, py + dy
            if 0 <= npx < n and 0 <= npy < m and data[npx][npy] == value + 1:
                res += get_score(npx, npy)
        dp[px][py] = res
        return res
    
    ans = 0
    for i in range(n):
        for j in range(m):
            if data[i][j] == 0:
                ans += get_score(i, j)
    return ans

if __name__ == "__main__":
    # print(part1())
    print(part2())