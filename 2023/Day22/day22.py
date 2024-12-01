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


def is_overlap(brick1, brick2):
	return max(brick1[0], brick2[0]) <= min(brick1[3], brick2[3]) and \
				max(brick1[1], brick2[1]) <= min(brick1[4], brick2[4])

def settle_bricks(bricks):
	bricks.sort(key=lambda x: x[2])
	for i, brick1 in enumerate(bricks):
		pos_z = 1
		for brick2 in bricks[:i]:
				if is_overlap(brick1, brick2):
					pos_z = max(pos_z, brick2[-1] + 1)
		diff = brick1[-1] - brick1[2]
		brick1[2] = pos_z
		brick1[-1] = pos_z + diff
	bricks.sort(key=lambda x: x[2])

def part1():
	bricks = []
	with open("input.txt", "r") as fp:
		for line in fp:
			coords = line.strip().replace("~", ",").split(",")
			bricks.append([int(coord) for coord in coords])

	settle_bricks(bricks)
	n = len(bricks)
	supports = [set() for _ in range(n)]
	supported_by = [set() for _ in range(n)]
	for i, top in enumerate(bricks):
		for j, bottom in enumerate(bricks[:i]):
			if is_overlap(top, bottom) and bottom[-1] + 1 == top[2]:
				supports[j].add(i)
				supported_by[i].add(j)
	ans = 0
	for i in range(n):
		if all(len(supported_by[j]) > 1 for j in supports[i]):
			ans += 1
	return ans


def part2():
	bricks = []
	with open("input.txt", "r") as fp:
		for line in fp:
			coords = line.strip().replace("~", ",").split(",")
			bricks.append([int(coord) for coord in coords])

	settle_bricks(bricks)
	n = len(bricks)
	supports = [set() for _ in range(n)]
	supported_by = [set() for _ in range(n)]
	for i, top in enumerate(bricks):
		for j, bottom in enumerate(bricks[:i]):
			if is_overlap(top, bottom) and bottom[-1] + 1 == top[2]:
				supports[j].add(i)
				supported_by[i].add(j)
	
	ans = 0
	for i in range(n):
		q = deque([])
		seen = set()
		for j in supports[i]:
			if len(supported_by[j]) == 1:
				q.append(j)
				seen.add(j)
		
		while q:
			curr = q.popleft()
			for nxt in supports[curr] - seen:
				if supported_by[nxt].issubset(seen):
					q.append(nxt)
					seen.add(nxt)
		ans += len(seen)
	return ans


if __name__ == "__main__":
    # print(part1())
    print(part2())
