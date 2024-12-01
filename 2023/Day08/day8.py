from collections import Counter
import math 
import os 
try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass 

def part1():
	inst = ""
	mp = {}
	with open("input.txt", "r") as fp:
		inst = fp.readline().strip()
		fp.readline()
		for line in fp.readlines():
			line = line.strip().split()
			mp[line[0]] = (line[2][1:-1], line[3][:-1])
	n = len(inst)
	idx = 0
	ans = 0
	start = "AAA"
	while start != "ZZZ":
		ans += 1
		if inst[idx] == "L":
			start = mp[start][0]
		else:
			start = mp[start][1]
		idx = (idx + 1) % n
	return ans

def part2():
	inst = ""
	mp = {}
	nodes = []
	N = None 
	
	def parse_input():
		nonlocal inst, mp
		with open("input.txt", "r") as fp:
			inst = fp.readline().strip()
			fp.readline()
			for line in fp.readlines():
				line = line.strip().split()
				mp[line[0]] = (line[2][1:-1], line[3][:-1])
				if line[0][-1] == "A":
					nodes.append(line[0])

	def get_cycle_length(node):
		idx = 0
		count = 0
		N = len(inst)
		while not node.endswith("Z"):
			count += 1
			pos = 0 if inst[idx] == "L" else 1
			node = mp[node][pos]
			idx = (idx + 1) % N 

		return count
	
		# first_z = None 
		# cycles = []
		# while True:
		# 	while count == 0 or not node.endswith("Z"):
		# 		count += 1
		# 		pos = 0 if inst[idx] == "L" else 1
		# 		node = mp[node][pos]
		# 		idx = (idx + 1) % N
			
		# 	cycles.append(count)
		# 	if first_z is None:
		# 		first_z = node 
		# 		count = 0
		# 	elif node == first_z:
		# 		break
		# return cycles 

	parse_input()
	lcm = 1
	for node in nodes:
		res = get_cycle_length(node)
		lcm = math.lcm(lcm, res)
	return lcm

if __name__ == "__main__":
	# print(part1())
	print(part2())
