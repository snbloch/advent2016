import io

instructions = []
registers = {}
for reg in 'abd':
    registers[reg] = 0
registers['c'] = 1

file = open('input.txt', 'r')
for line in file:
    instructions.append(line.strip())

position = 0
while position < len(instructions):
    #print position, instructions[position], registers
    if 'cpy' in instructions[position]:
        reg_or_val = instructions[position].split()[1]
        target_reg = instructions[position].split()[2]
        if reg_or_val in 'abcd':
            registers[target_reg] = registers[reg_or_val]
        else:
            registers[target_reg] = int(reg_or_val)
        position += 1
    elif 'inc' in instructions[position]:
        target_reg = instructions[position].split()[1]
        registers[target_reg] += 1
        position += 1
    elif 'dec' in instructions[position]:
        target_reg = instructions[position].split()[1]
        registers[target_reg] -= 1
        position += 1
    elif 'jnz' in instructions[position]:
        reg_or_val = instructions[position].split()[1]
        jump = int(instructions[position].split()[2])
        if reg_or_val in 'abcd':
            val = registers[reg_or_val]
        else:
            val = int(reg_or_val)
        if val != 0:
            position += jump
        else:
            position += 1

print registers
