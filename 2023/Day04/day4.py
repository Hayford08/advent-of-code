# part 1
# with open("input.txt", "r") as fp:
#     for line in fp.readlines():
#         group = line.strip()[line.find(":") + 1: ].split("|")
#         winning_numbers = set(int(num) for num in group[0].split() if num != "")
#         cnt = 0
#         for val in group[1].split():
#             if val != "" and int(val) in winning_numbers:
#                 cnt += 1
#                 if cnt == 0:
#                     cnt += 1
#                 else:
#                     cnt *= 2
#         ans += cnt


# part 2
from collections import defaultdict
ans = 0
mp = defaultdict(int)
with open("input.txt", "r") as fp:
    card = 1
    for line in fp.readlines():
        group = line.strip()[line.find(":") + 1: ].split("|")
        winning_numbers = set(int(num) for num in group[0].split() if num != "")
        cnt = 0
        for val in group[1].split():
            if val != "" and int(val) in winning_numbers:
                cnt += 1
        mp[card] += 1
        if cnt > 0:
            for nc in range(card + 1, card + cnt + 1):
                mp[nc] += mp[card]
        ans += mp[card]
        card += 1

print(ans)