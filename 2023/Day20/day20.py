from collections import deque
import os
import sys
from math import lcm
sys.setrecursionlimit(10000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

# Got inspiration from HyperNeutrino: https://www.youtube.com/watch?v=lxm6i21O83k
BROADCASTER = "broadcaster"
RX = "rx"
FLIPFLOP = "%"
CONJUNCTION = "&"
OFF = 0
ON = 1
LOW = 0
HIGH = 1

class Module:
	def __init__(self, name, type, targets) -> None:
		self.name = name 
		self.type = type
		self.targets = targets
		if type == FLIPFLOP:
			self.state = OFF
		else:
			self.most_recent_pulses = {}

def part1():
	modules = {}
	broadcast_targets = []
	with open("input.txt", "r") as fp:
		for line in fp:
			left, right = line.strip().split(" -> ")
			targets = right.split(", ")
			if left == BROADCASTER:
				broadcast_targets = targets
			else:
				type, name = left[0], left[1:]
				modules[name] = Module(name, type, targets)
	
	for name, module in modules.items():
		for target in module.targets:
			if target in modules and modules[target].type == CONJUNCTION:
				modules[target].most_recent_pulses[name] = LOW

	count = [0, 0]
	for _ in range(1000):
		count[LOW] += 1
		# src, dest, pulse
		q = deque([(BROADCASTER, name, LOW) for name in broadcast_targets])
		while q:
			src, dest, pulse = q.popleft()
			count[pulse] += 1
			if dest not in modules:
				continue
			module = modules[dest]
			if module.type == CONJUNCTION:
				module.most_recent_pulses[src] = pulse 
				pulse_to_send = LOW if all(module.most_recent_pulses.values()) else HIGH
				for target in module.targets:
					q.append((module.name, target, pulse_to_send))

			elif pulse == LOW:
					pulse_to_send = LOW if module.state else HIGH
					module.state ^= 1
					for target in module.targets:
						q.append((module.name, target, pulse_to_send))
	return count[0] * count[1]

def part2():
	modules = {}
	broadcast_targets = []
	feed = None
	with open("input.txt", "r") as fp:
		for line in fp:
			left, right = line.strip().split(" -> ")
			targets = right.split(", ")
			if left == BROADCASTER:
				broadcast_targets = targets
			else:
				type, name = left[0], left[1:]
				modules[name] = Module(name, type, targets)
				if RX in targets:
					feed = name

	button_presses = 0
	cycle_lengths = {}
	seen = {}
	for name, module in modules.items():
		for target in module.targets:
			if target in modules and modules[target].type == CONJUNCTION:
				modules[target].most_recent_pulses[name] = LOW
		if feed in module.targets:
			seen[name] = 0

	while True:
		button_presses += 1
		# src, dest, pulse
		q = deque([(BROADCASTER, name, LOW) for name in broadcast_targets])
		while q:
			src, dest, pulse = q.popleft()
			if dest not in modules:
				continue
			module = modules[dest]
			if module.name == feed and pulse == HIGH:
				seen[src] += 1
				if src not in cycle_lengths:
					cycle_lengths[src] = button_presses
				else:
					assert button_presses == seen[src] * cycle_lengths[src]

				if all(seen.values()):
					ans = 1
					for x in cycle_lengths.values():
						ans = lcm(ans, x)
					return ans 

			if module.type == CONJUNCTION:
				module.most_recent_pulses[src] = pulse 
				pulse_to_send = LOW if all(module.most_recent_pulses.values()) else HIGH
				for target in module.targets:
					q.append((module.name, target, pulse_to_send))

			elif pulse == LOW:
					pulse_to_send = LOW if module.state else HIGH
					module.state ^= 1
					for target in module.targets:
						q.append((module.name, target, pulse_to_send))
	

if __name__ == "__main__":
	# print(part1())
	print(part2())
