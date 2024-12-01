from collections import Counter
import os
import sys
import math
sys.setrecursionlimit(20000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass
MP = {
	"U" : (-1, 0),
	"D" : (1, 0),
	"L"	: (0, -1),
	"R"	: (0, 1),
}

NUM_TO_MP = {
	"0": "R",
	"1": "D",
	"2": "L",
	"3": "U",
}


# Topics needed: shoelace formula and Pick's theorem 
# https://en.wikipedia.org/wiki/Shoelace_formula
# https://en.wikipedia.org/wiki/Pick%27s_theorem

def calculate(points, B):
	N = len(points)
	A = abs(sum([points[i][0] * (points[(i + 1) % N][1] - points[i - 1][1]) for i in range(N)])) // 2
	I = A - B // 2 + 1
	return I + B

def part1():
	points = [(0, 0)]
	B = 0
	with open("input.txt", "r") as fp:
		for line in fp:
			dir, cnt, _ = line.split()
			cnt = int(cnt)
			B += cnt
			dx, dy = MP[dir]
			x, y = points[-1]
			points.append((x + cnt * dx, y + cnt * dy))

	return calculate(points, B)

def part2():
	points = [(0, 0)]
	B = 0
	with open("input.txt", "r") as fp:
		for line in fp:
			_, _, code = line.split()
			code = code[1:-1]
			dir = code[-1]
			cnt = int(code[1 : -1], 16)
			B += cnt
			x, y = points[-1]
			dx, dy = MP[NUM_TO_MP[dir]]
			points.append((x + cnt * dx, y + cnt * dy))
			
	return calculate(points, B)


if __name__ == "__main__":
	# print(part1())
	print(part2())
