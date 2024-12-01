from collections import Counter
import os
import math
try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

def part1():
	data = []
	with open("input.txt", "r") as fp:
		data = fp.readlines()
	
	def get_diff(values):
		return [x - y for x, y in zip(values[1:], values)]

	def solve(seq):
		values = [int(num) for num in seq.split() if num != ""]
		diff = get_diff(values)
		last = [values[-1]]
		while True:
			last.append(diff[-1])
			if len(set(diff)) == 1:
				break 
			diff = get_diff(diff)
		ans = 0
		for x in reversed(last):
			ans += x 
		return ans
	
	return sum(list(solve(seq) for seq in data))

def part2():
	data = []
	with open("input.txt", "r") as fp:
		data = fp.readlines()
	
	def get_diff(values):
		return [x - y for x, y in zip(values, values[1:])]

	def solve(seq):
		values = [int(num) for num in seq.split() if num != ""][::-1]
		diff = get_diff(values)
		last = [values[-1]]
		while True:
			last.append(diff[-1])
			if len(set(diff)) == 1:
				break
			diff = get_diff(diff)
		ans = 0
		for x in reversed(last):
			ans = x - ans
		return ans

	ans = 0
	for seq in data:
		ans += solve(seq)
	return ans


if __name__ == "__main__":
	print(part1())
	print(part2())
