ans = 0
mp = {"one": 1, "two" : 2, "three" : 3, "four" : 4, "five" : 5, "six" : 6, "seven" : 7, "eight" : 8, "nine" : 9}
with open("input.txt", "r") as fb:
    for line in fb.readlines():
        values = []
        prev = 0
        for i, c in enumerate(line):
            if c.isdigit():
                values.append(int(c))
            
            elif i >= 2:
                for j in range(3, 6):
                    if j - 1 > i:
                        break 
                    start = max(prev, i - j + 1)
                    s = line[max(prev, i - j + 1) : min(i + 1, start + j)]
                    if s in mp:
                        values.append(mp[s])
                        break
        ans += 10 * values[0] + values[-1]

print(ans)



