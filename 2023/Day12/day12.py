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

def part1():

	def solve(i, j, data, sequence, dp):
		if  i >= len(data):
			return 1 if j == len(sequence) else 0
		
		if j == len(sequence):
			return 0 if "#" in data[i:] else 1
		
		try:
			return dp[(i, j)]
		except KeyError:
			ans = 0
			if data[i] in "?.":
				ans = solve(i + 1, j, data, sequence, dp)
			
			if data[i] in "#?":
				sz = sequence[j]
				if sz <= len(data) - i and "." not in data[i: i + sz] and (len(data) == sz + i or data[i + sz] != "#"):
					ans += solve(i + sz + 1, j + 1, data, sequence, dp)
			dp[(i, j)] = ans 
			return ans

	ans = 0
	with open("input.txt", "r") as fp:
		for line in fp.readlines():
			line = line.strip()
			data, sequence = line.split(" ")
			sequence = [int(num) for num in sequence.split(",") if num]
			ans += solve(0, 0, data, sequence, {})
	return ans 

def part2():
	def solve(i, j, data, sequence, dp):
		if  i >= len(data):
			return 1 if j == len(sequence) else 0
		
		if j == len(sequence):
			return 0 if "#" in data[i:] else 1
		
		try:
			return dp[(i, j)]
		except KeyError:
			ans = 0
			if data[i] in "?.":
				ans = solve(i + 1, j, data, sequence, dp)
			
			if data[i] in "#?":
				sz = sequence[j]
				if sz <= len(data) - i and "." not in data[i: i + sz] and (len(data) == sz + i or data[i + sz] != "#"):
					ans += solve(i + sz + 1, j + 1, data, sequence, dp)
			dp[(i, j)] = ans
			return ans

	ans = 0
	with open("input.txt", "r") as fp:
		for line in fp.readlines():
			line = line.strip()
			data, sequence = line.split(" ")
			data = "?".join([data for _ in range(5)])
			sequence = [int(num) for num in sequence.split(",") if num]
			sequence = sequence * 5
			ans += solve(0, 0, data, sequence, {})
	return ans 

if __name__ == "__main__":
	# print(part1())
	print(part2())
