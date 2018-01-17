import math
import io

instructions = []
input_value = 12

file = open('input.txt', 'r')
for line in file:
    instructions.append(line.strip())

position = 0
while position < len(instructions):
    if instructions[position][0:3] == 'cpy' and instructions[position + 1][0:3] == 'jnz' and int(instructions[position].split()[1]) > 0 and int(instructions[position + 1].split()[1]) > 0:
        magic_number = int(instructions[position].split()[1]) * int(instructions[position + 1].split()[1])
        break
    position += 1

print magic_number + math.factorial(input_value)
