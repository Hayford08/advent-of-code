import os
import sys
sys.setrecursionlimit(20000)

try:
	current_file_directory = os.path.dirname(os.path.abspath(__file__))
	os.chdir(current_file_directory)
except:
	pass

def part1():
	graph = nx.Graph()
	with open("input.txt", "r") as fp:
		for line in fp:
			name, components = line.strip().split(": ")
			for nei in components.split(" "):
				graph.add_edge(name, nei)
				graph.add_edge(nei, name)

	graph.remove_edges_from(nx.minimum_edge_cut(graph))
	comp1, comp2 = list(nx.connected_components(graph))
	return len(comp1) * len(comp2)

def part2():
	return "HAPPY HOLIDAYS!!!!!"

if __name__ == "__main__":
	print(part1())
	print(part2())
