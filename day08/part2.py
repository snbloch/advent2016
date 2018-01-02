import io
import numpy

instructions = []
screen_width = 50
screen_height = 6

file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    instruction = []
    verb = line.split()[0]
    if verb == 'rect':
        instruction.append(verb)
        width = int(line.split()[1].split('x')[0])
        height = int(line.split()[1].split('x')[1])
        instruction.append(width)
        instruction.append(height)
    elif verb == 'rotate':
        instruction.append(verb)
        rotation_type = line.split()[1]
        index = int(line.split('=')[1].split()[0])
        shift = int(line.split(' by ')[1])
        instruction.append(rotation_type)
        instruction.append(index)
        instruction.append(shift)
    instructions.append(instruction)

screen = numpy.zeros((screen_height, screen_width))

for instruction in instructions:
    if instruction[0] == 'rect':
        current_y = 0
        while current_y < instruction[2]:
            current_x = 0
            while current_x < instruction[1]:
                screen[current_y][current_x] = 1
                current_x += 1
            current_y += 1
    elif instruction[0] == 'rotate':
        rotation_count = 0
        while rotation_count < instruction[3]:
            if instruction[1] == 'row':
                temp_row = []
                for i in screen[instruction[2]]:
                    temp_row.append(i)
                row_position = 0
                while row_position < len(temp_row):
                    if row_position == len(temp_row) - 1:
                        screen[instruction[2]][0] = temp_row[row_position]
                    else:
                        screen[instruction[2]][row_position + 1] = temp_row[row_position]
                    row_position += 1
            elif instruction[1] == 'column':
                temp_column = []
                column_position = instruction[2]
                row_counter = 0
                while row_counter < screen_height:
                    temp_column.append(screen[row_counter][column_position])
                    row_counter += 1
                row_counter = 0
                while row_counter < screen_height:
                    if row_counter == len(temp_column) - 1:
                        screen[0][column_position] = temp_column[row_counter]
                    else:
                        screen[row_counter + 1][column_position] = temp_column[row_counter]
                    row_counter += 1
            rotation_count += 1

screen_output = ''
row_counter = 0
while row_counter < screen_height:
    for i in screen[row_counter]:
        if i == 1:
            screen_output += '#'
        else:
            screen_output += ' '
    screen_output += '\n'
    row_counter += 1

print screen_output
