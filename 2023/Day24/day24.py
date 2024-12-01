from collections import Counter, deque, defaultdict
import os
import sys
from math import gcd
import sympy
sys.setrecursionlimit(20000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass


def point_of_intersection(a, b):
	# parallel lines
	if a[3] * b[4] == a[4] * b[3]:
		return None

	m1 = a[4] / a[3]
	m2 = b[4] / b[3]

	x1, y1, x2, y2 = a[0], a[1], b[0], b[1]

	x = (y1 - y2 - m1 * x1 + m2 * x2) / (m2 - m1)
	return (x, y1 + m1 * (x - x1))


def within_bounds(pt):
	LEFT_BOUND, RIGHT_BOUND = 200000000000000, 400000000000000
	for x in pt:
		if not (LEFT_BOUND <= x <= RIGHT_BOUND):
			return False
	return True

def is_future(new_pt, a):
	return ((new_pt[0] - a[0]) / a[3]) >= 0


def part1():
	hailstones = []
	with open("input.txt", "r") as fp:
		for line in fp:
			hailstones.append(list(map(int, line.strip().replace(" @ ", ", ").split(", "))))

	ans = 0
	for i, a in enumerate(hailstones):
		for b in hailstones[i + 1: ]:
			pt = point_of_intersection(a, b)
			if pt is not None and within_bounds(pt) and is_future(pt, a) and is_future(pt, b):
				ans += 1
	return ans

def part2():
	hailstones = []
	with open("input.txt", "r") as fp:
		for line in fp:
			hailstones.append(list(map(int, line.strip().replace(" @ ", ", ").split(", "))))

	rpx, rpy, rpz, rvx, rvy, rvz = sympy.symbols("rpx, rpy, rpz, rvx, rvy, rvz")

	eqns = []
	for px, py, pz, vx, vy, vz in hailstones:
		eqns.append((rpx - px) * (vy - rvy) - (vx - rvx) * (rpy - py))
		eqns.append((rpy - py) * (vz - rvz) - (vy - rvy) * (rpz - pz))

	result = sympy.solve(eqns)[0]
	ans = 0
	for key in [rpx, rpy, rpz]:
		ans += result[key]
	return ans

if __name__ == "__main__":
	# print(part1())
	print(part2())
