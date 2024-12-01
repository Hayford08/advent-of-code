# from collections import defaultdict
# ans = 0
# arr = []
# DX = [-1, -1, -1, 0, 0, 1, 1, 1]
# DY = [-1, 0, 1, -1, 1, -1, 0, 1]

# with open("input.txt", "r") as fp:
#     for line in fp.readlines():
#         arr.append(line.strip())

# n, m  = len(arr), len(arr[0])
# is_symbol = [[False for _ in range(m)] for _ in range(n)]

# g = {defaultdict(list)}
# for i in range(n):
#     j = 0
#     while j < m:
#         if arr[i][j] == '.':
#             j += 1
#         elif not arr[i][j].isdigit():
#             is_symbol[i][j] = True
#             j += 1
#         else:
#             pos = [(i, j)]
#             num = int(arr[i][j])
#             nj = j + 1
#             while nj < m and arr[i][nj].isdigit():
#                 num = num * 10 + int(arr[i][nj])
#                 pos.append((i, nj))
#                 nj += 1
#             j = nj
#             g[num].append(pos)

# for k, v in g.items():
#     for pos_list in v:
#         flag = False 
#         for x, y in pos_list:
#             if flag:
#                 break
#             for i in range(8):
#                 nx = x + DX[i]
#                 ny = y + DY[i]
#                 if 0 <= nx < n and 0 <= ny < m and is_symbol[nx][ny]:
#                     flag = True
#                     break
#         if flag:
#             ans += k

# print(ans)


# part 2
from collections import defaultdict
ans = 0
arr = []
DX = [-1, -1, -1, 0, 0, 1, 1, 1]
DY = [-1, 0, 1, -1, 1, -1, 0, 1]

with open("input.txt", "r") as fp:
    for line in fp.readlines():
        arr.append(line.strip())

n, m  = len(arr), len(arr[0])
is_symbol = [[False for _ in range(m)] for _ in range(n)]

g = {}
numbers = defaultdict(list)
for i in range(n):
    j = 0
    while j < m:
        if arr[i][j] == '*':
            g[(i, j)] = [0, 1]
            is_symbol[i][j] = True
            j += 1
        elif not arr[i][j].isdigit():
            j += 1
        else:
            pos = [(i, j)]
            num = int(arr[i][j])
            nj = j + 1
            while nj < m and arr[i][nj].isdigit():
                num = num * 10 + int(arr[i][nj])
                pos.append((i, nj))
                nj += 1
            j = nj
            numbers[num].append(pos)

for k, v in numbers.items():
    for pos_list in v:
        flag = False 
        for x, y in pos_list:
            if flag:
                break
            for i in range(8):
                nx = x + DX[i]
                ny = y + DY[i]
                if 0 <= nx < n and 0 <= ny < m and is_symbol[nx][ny]:
                    g[(nx, ny)][0] += 1
                    g[(nx, ny)][1] *= k
                    flag = True
                    break

for _, v in g.items():
    if v[0] == 2:
        ans += v[1]
print(ans)