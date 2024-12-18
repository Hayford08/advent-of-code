from collections import Counter, deque, defaultdict
import os
import sys
import re
import math

sys.setrecursionlimit(20000)

try:
    current_file_directory = os.path.dirname(os.path.abspath(__file__))
    os.chdir(current_file_directory)
except:
    pass

def get_input():
    with open("input.txt", "r") as fp:
        return fp.read().strip().split("\n\n")
    
def parse_input():
    registers, instructions = get_input()
    pattern = r"Register A: (\d+)\nRegister B: (\d+)\nRegister C: (\d+)"
    registers = list(map(int, re.match(pattern, registers).groups()))
    instructions = instructions[8:].split(',')
    instructions = list(map(int, instructions))
    return registers, instructions

A, B, C = 0, 1, 2

def fetch_value(operand, registers):
    if operand <= 3:
        return operand
    return registers[operand - 4]

def execute(registers, instructions):
    result = []
    ip = 0
    while ip < len(instructions):
        opcode = instructions[ip]
        operand = instructions[ip + 1]
        if opcode == 0:
            registers[A] >>= fetch_value(operand, registers)
            ip += 2
        elif opcode == 1:
            registers[B] ^= operand
            ip += 2
        elif opcode == 2:
            registers[B] = fetch_value(operand, registers) & 0b111
            ip += 2
        elif opcode == 3:
            if registers[A] == 0:
                ip += 2
            else:
                ip = operand
        elif opcode == 4:
            registers[B] ^= registers[C]
            ip += 2
        elif opcode == 5:
            result.append(fetch_value(operand, registers) & 0b111)
            ip += 2
        elif opcode == 6:
            registers[B] = registers[A] >> fetch_value(operand, registers)
            ip += 2
        else:
            registers[C] = registers[A] >> fetch_value(operand, registers)
            ip += 2
    return result

def part1():
    registers, instructions = parse_input()
    return ",".join(map(str, execute(registers, instructions)))

def part2():
    """
    This solution only works for the input given in the problem.
    However, it can be easily modified to work for any input based 
    on the instructions given in the problem.
    """
    _, instructions = parse_input()
    def backtrack(index, rega):
        if index < 0:
            return rega
        for a in range(8):
            a = (rega << 3) | a
            b = a % 8
            b = b ^ 3
            c = a >> b
            b = b ^ 5
            b = b ^ c
            if b % 8 == instructions[index]:
                val = backtrack(index - 1, a)
                if val is not None:
                    return val
        return None
    
    return backtrack(len(instructions) - 1, 0)

if __name__ == "__main__":
    # print(part1())
    print(part2())