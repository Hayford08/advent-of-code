
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

ans = 0
left, right = [], []
with open("input.txt", "r") as fp:
    for line in fp.readlines():
        line = line.strip()
        x, y = line.split()
        left.append(int(x))
        right.append(int(y))

left.sort()
right.sort()

for x, y in zip(left, right):
    ans += abs(x - y)
print(ans)

## Part 2
ans = 0
right_map = Counter(right)
for x in left:
    ans += x * right_map[x]

print(ans)