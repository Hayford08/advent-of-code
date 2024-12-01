from collections import defaultdict
def part1():
    maps = [[] for _ in range(7)]
    map_names = ["seed-to-soil map", "soil-to-fertilizer map", "fertilizer-to-water map", "water-to-light map", "light-to-temperature map", "temperature-to-humidity map", "humidity-to-location map", "###"]
    seeds = set()

    def process():
        nonlocal seeds
        start_index = -1
        with open("input.txt", "r") as fp:
            line1 = fp.readline()
            seeds = [int(num) for num in line1[line1.find(":") + 1: ].strip().split() if num != ""]
            for line in fp.readlines():
                line = line.strip()
                if not line:
                    continue

                if line.startswith(map_names[start_index + 1]):
                    start_index += 1
                    continue
                dest, src, length = [int(num) for num in line.strip().split() if num != ""]
                maps[start_index].append((src, dest, length))

    def solve(u, idx):
        if idx == len(maps):
            return u
    
        for (src, dest, length) in maps[idx]:
            if src <= u < src + length:
                return solve(dest + u - src, idx + 1)
        return solve(u, idx + 1)
    
    process()
    ans = float("inf")
    for seed in seeds:
        ans = min(ans, solve(seed, 0))
    return ans 

def part2():
    def get_blocks():
        blocks = []
        with open("input.txt", "r") as fp:
            blocks = fp.read().split("\n\n")
        return blocks

    def blocks_data(blocks):
        result = []
        for block in blocks:
            tmp = []
            for line in block.splitlines()[1:]:
                dest, src, length = map(int, line.split())
                tmp.append((src, dest, length))
            result.append(tmp)
        return result
    
    def parse_seeds(seeds):
        res = []
        for i in range(0, len(seeds), 2):
            res.append((seeds[i], seeds[i] + seeds[i + 1]))
        return res 
    
    def solve(seeds, blocks):
        for block in blocks:
            new_seeds = []
            while seeds:
                s, e = seeds.pop()
                for src, dest, length in block:
                    ns = max(s, src)
                    ne = min(e, src + length)
                    if ns < ne:
                        new_seeds.append((dest + ns - src, dest + ne - src))

                        if ns > s:
                            seeds.append((s, ns))
                        
                        if e > ne:
                            seeds.append((ne, e))
                        break 
                else:
                    new_seeds.append((s, e))
            seeds = new_seeds
        return min(seeds)[0]
    
    seeds, *blocks = get_blocks()
    blocks = blocks_data(blocks)
    seeds = parse_seeds(list(map(int, seeds.split(":")[1].split())))
    return solve(seeds, blocks)

if __name__ == "__main__":
    # print(part1())
    print(part2())