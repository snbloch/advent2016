import io

instructions = []
registers = {}
for reg in 'abcd':
    registers[reg] = 0
    registers['a'] = 7

file = open('input.txt', 'r')
for line in file:
    instructions.append(line.strip())

position = 0
while position < len(instructions):
    print position, instructions[position], registers
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
        try:
            jump = int(instructions[position].split()[2])
        except ValueError:
            jump = int(registers[instructions[position].split()[2]])
        if reg_or_val in 'abcd':
            val = registers[reg_or_val]
        else:
            val = int(reg_or_val)
        if val != 0:
            position += jump
        else:
            position += 1
    elif 'tgl' in instructions[position]:
        jump = int(registers[instructions[position].split()[1]])
        target_reg = position + jump
        try:
            original_instruction = instructions[target_reg]
        except IndexError:
            position += 1
            continue
        original_instruction_verb = original_instruction[0:3]
        if len(original_instruction.split()) == 2:
            if original_instruction_verb == 'inc':
                new_instruction_verb = 'dec'
            else:
                new_instruction_verb = 'inc'
        elif len(original_instruction.split()) == 3:
            if original_instruction_verb == 'jnz':
                new_instruction_verb = 'cpy'
            else:
                new_instruction_verb = 'jnz'
        new_instruction = original_instruction.replace(original_instruction_verb, new_instruction_verb)
        instructions[target_reg] = new_instruction
        position += 1

print registers
