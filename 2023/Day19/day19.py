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
	
def apply_flow(mappings, workflow, flow_name):
	if flow_name == "A":
		return True
	if flow_name == "R":
		return False
	flow, fall_back = workflow[flow_name]
	for key, cmp, val, dest in flow:
		if cmp(mappings[key], val):
			return apply_flow(mappings, workflow, dest)
	return apply_flow(mappings, workflow, fall_back)

def count_combinations(mappings, workflow, flow_name):
	if flow_name == "A":
		res = 1
		for l, r in mappings.values():
			res *= r - l + 1
		return res
	
	if flow_name == "R":
		return 0
	
	flow, fall_back = workflow[flow_name]
	res = 0
	use_fall_back = True 
	for key, cmp, val, dest in flow:
		l, r = mappings[key]
		if cmp == "<":
			true_case = (l, val - 1)
			false_case = (val, r)
		else:
			true_case = (val + 1, r)
			false_case = (l, val)
		
		if true_case[0] <= true_case[1]:
			new_mappings = dict(mappings)
			new_mappings[key] = true_case
			res += count_combinations(new_mappings, workflow, dest)
		
		if false_case[0] <= false_case[1]:
			mappings = dict(mappings)
			mappings[key] = false_case
		else:
			use_fall_back = False
			break

	if use_fall_back:
		res += count_combinations(mappings, workflow, fall_back)
	return res

def part1():
	blocks = []
	with open("input.txt", "r") as fp:
		blocks = fp.read().strip().split("\n\n")
	
	instructions, values = blocks
	instructions = instructions.splitlines()
	workflow = {}
	for instruction in instructions:
		index = instruction.find("{")
		name = instruction[:index]
		rules = instruction[index + 1:-1].split(",")
		fall_back = rules.pop()
		flow = []
		for rule in rules:
			cond, dest = rule.split(":")
			key, cmp, val = cond[0], cond[1], int(cond[2:])
			cmp = (lambda x, y : x < y) if cmp == "<" else (lambda x, y: x > y)
			flow.append((key, cmp, val, dest))
		workflow[name] = (flow, fall_back)
	
	ans = 0
	for line in values.splitlines():
		items = line[1:-1].split(",")
		mappings = {}
		for item in items:
			key, value = item.split("=")
			mappings[key] = int(value)
		
		if apply_flow(mappings, workflow, "in"):
			ans += sum(mappings.values())

	return ans

def part2():
	blocks = []
	with open("input.txt", "r") as fp:
		blocks = fp.read().strip().split("\n\n")
	
	instructions, _ = blocks
	instructions = instructions.splitlines()
	workflow = {}
	for instruction in instructions:
		index = instruction.find("{")
		name = instruction[:index]
		rules = instruction[index + 1:-1].split(",")
		fall_back = rules.pop()
		flow = []
		for rule in rules:
			cond, dest = rule.split(":")
			key, cmp, val = cond[0], cond[1], int(cond[2:])
			flow.append((key, cmp, val, dest))
		workflow[name] = (flow, fall_back)

	return count_combinations({key: (1, 4000) for key in "xmas"}, workflow, "in")

if __name__ == "__main__":
	print(part1())
	print(part2())
