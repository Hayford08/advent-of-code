import sys 
import os 
if __name__ == "__main__":
	if len(sys.argv) == 1:
		raise Exception("Need filename to create")
	try:
		day, inp = sys.argv[1], sys.argv[2]
	except IndexError:
		print("Need to pass in the correct amount of argv i.e. 3 --> [aoc.py aoc_day aoc_day_input]")
	try:
		os.makedirs(f"Day{day}")
	except FileExistsError:
		pass 
	with open(f"Day{day}/input.txt", "w") as fp:
		fp.write(inp)

	with open(f"Day{day}/day{day}.py", "w") as fp:
		fp.write("from collections import Counter, deque, defaultdict\n")
		fp.write("import os\n")
		fp.write("import sys\n")
		fp.write("import math\n")
		fp.write("sys.setrecursionlimit(20000)\n\n")
		fp.write("try:\n\tcurrent_file_directory = os.path.dirname(os.path.abspath(__file__))\n")
		fp.write("\tos.chdir(current_file_directory)\n")
		fp.write("except:\n")
		fp.write("\tpass\n\n")
		fp.write("def part1():\n")
		fp.write("\twith open(\"input.txt\", \"r\") as fp:\n")
		fp.write("\t\tpass\n\n")
		fp.write("def part2():\n")
		fp.write("\twith open(\"input.txt\", \"r\") as fp:\n")
		fp.write("\t\tpass\n\n")
		fp.write("if __name__ == \"__main__\":\n")
		fp.write("\tprint(part1())\n")
		fp.write("\tprint(part2())\n")


    