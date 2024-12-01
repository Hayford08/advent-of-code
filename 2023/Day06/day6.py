from collections import defaultdict
def part1():
    data = []
    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            data.append(list(map(int, line[line.find(":") + 1 : ].split())))
    ans = 1
    n = len(data[0])
    for i in range(n):
        t, d = data[0][i], data[1][i]
        l,r = -1, -1
        for j in range(1, t):
            dist = (t - j) * j
            if dist > d:
                if l == -1:
                    l = j 
                r = j
        if l == -1:
            ans = 0
            break 
        ans *= (r - l + 1)
    return ans 

def part2():
    data = []
    with open("input.txt", "r") as fp:
        for line in fp.readlines():
            data.append(int("".join(line[line.find(":") + 1: ].split())))
    
    def find_left(t, d):
        l, r = 0, t 
        ans = -1
        while l <= r:
            mid = int(l + (r - l) / 2)
            if (t - mid) * mid > d:
                ans = mid 
                r = mid - 1
            else:
                l = mid + 1
        return ans
    
    def find_right(t, d):
        l, r = 0, t
        ans = -1
        while l <= r:
            mid = int(l + (r - l) / 2)
            if (t - mid) * mid > d:
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        return ans

    l = find_left(*data)
    if l == -1:
        return 0
    return find_right(*data) - l + 1


if __name__ == "__main__":
    # print(part1())
    print(part2())