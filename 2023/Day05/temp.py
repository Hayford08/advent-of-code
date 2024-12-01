inputs, *blocks = open("input.txt").read().split("\n\n")

inputs = list(map(int, inputs.split(":")[1].split()))

seeds = []

for i in range(0, len(inputs), 2):
    seeds.append((inputs[i], inputs[i] + inputs[i + 1]))

for block in blocks:
    ranges = []
    for line in block.splitlines()[1:]:
        ranges.append(list(map(int, line.split())))
    new = []
    print(block)
    print()
    while len(seeds) > 0:
        s, e = seeds.pop()
        for dest, src, length in ranges:
            ns = max(s, src)
            ne = min(e, src + length)
            if ns < ne:
                new.append((ns - src + dest, ne - src + dest))
                if ns > s:
                    seeds.append((s, ns))
                if e > ne:
                    seeds.append((ne, e))
                break
        else:
            new.append((s, e))
    seeds = new

print(min(seeds)[0])