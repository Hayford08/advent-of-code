from collections import Counter
import os
import sys
import math
sys.setrecursionlimit(10000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

def hash(word):
	res = 0
	for ch in word:
		res += ord(ch)
		res *= 17
		res %= 256
	return res

def part1():
	words = []
	with open("input.txt", "r") as fp:
		words = fp.read().strip().split(",")
	
	return sum((map(hash, words)))

def part2():
	words = []
	with open("input.txt", "r") as fp:
		words = fp.read().strip().split(",")
	
	boxes = [set() for _ in range(256)]
	next_box_num = [0 for _ in range(256)]
	mp = {}
	for step in words:
		idx = step.find("=")
		if idx != -1:
			word = step[:idx]
			h = hash(word)
			f = int(step[idx + 1:])

			try:
				_, _, old_id = mp[word]
				mp[word] = (h, f, old_id)
			except KeyError:
				mp[word] = (h, f, next_box_num[h])
				boxes[h].add(next_box_num[h])
				next_box_num[h] += 1

		else:
			idx = step.find("-")
			word = step[:idx]
			h = hash(word)
			try:
				h, _, id = mp[word]
				del mp[word]
				boxes[h].remove(id)
			except KeyError:
				pass 

	boxes = [sorted(boxes[i]) for i in range(256)]
	slots = [{} for _ in range(256)]
	for i, box in enumerate(boxes):
		for j, id in enumerate(box):
			slots[i][id] = j + 1
	ans = 0
	for h, f, id in mp.values():
		ans += (h + 1) * slots[h][id] * f
	
	return ans

if __name__ == "__main__":
	# print(part1())
	print(part2())
