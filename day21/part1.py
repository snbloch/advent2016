import io

string = 'abcdefgh'
instructions = []

file = open('input.txt', 'r')
for line in file:
    inst = []
    if 'swap position' in line:
        inst.append('swap_position')
        inst.append(int(line.split()[2]))
        inst.append(int(line.split()[5]))
    elif 'swap letter' in line:
        inst.append('swap_letter')
        inst.append(line.split()[2])
        inst.append(line.split()[5])
    elif 'rotate left' in line or 'rotate right' in line:
        inst.append('rotate')
        inst.append(line.split()[1])
        inst.append(int(line.split()[2]))
    elif 'rotate based on position' in line:
        inst.append('rotate_position')
        inst.append(line.split()[6])
    elif 'reverse' in line:
        inst.append('reverse')
        inst.append(int(line.split()[2]))
        inst.append(int(line.split()[4]))
    elif 'move' in line:
        inst.append('move')
        inst.append(int(line.split()[2]))
        inst.append(int(line.split()[5]))
    instructions.append(inst)

def swap_position(a, b):
    copy = []
    for i in string:
        copy.append(i)
    copy[a] = string[b]
    copy[b] = string[a]
    return ''.join(copy)

def swap_letter(a, b):
    copy = []
    for i in string:
        copy.append(i)
    a_index = copy.index(a)
    b_index = copy.index(b)
    copy[a_index] = string[b_index]
    copy[b_index] = string[a_index]
    return ''.join(copy)

def rotate(dir, steps):
    copy = []
    for i in string:
        copy.append(i)
    counter = 0
    while counter < steps:
        temp = []
        if dir == 'right':
            temp.append(copy[-1])
            position = 0
            while position < len(copy) - 1:
                temp.append(copy[position])
                position += 1
        elif dir == 'left':
            position = 1
            while position < len(copy):
                temp.append(copy[position])
                position += 1
            temp.append(copy[0])
        copy = temp
        counter += 1
    return ''.join(copy)

def rotate_position(a):
    copy = []
    for i in string:
        copy.append(i)
    counter = 0
    a_index = copy.index(a)
    if a_index >= 4:
        target_rotations = a_index + 2
    else:
        target_rotations = a_index + 1
    while counter < target_rotations:
        temp = []
        temp.append(copy[-1])
        position = 0
        while position < len(copy) - 1:
            temp.append(copy[position])
            position += 1
        copy = temp
        counter += 1
    return ''.join(copy)

def reverse(a, b):
    copy = []
    for i in string:
        copy.append(i)
    to_reverse = copy[a:b + 1]
    reversed = []
    position = len(to_reverse) - 1
    while position >= 0:
        reversed.append(to_reverse[position])
        position -= 1
    position = a
    reversed_position = 0
    while position < b + 1:
        copy[position] = reversed[reversed_position]
        reversed_position += 1
        position += 1
    return ''.join(copy)

def move(a, b):
    copy = []
    for i in string:
        copy.append(i)
    to_move = copy.pop(a)
    copy.insert(b, to_move)
    return ''.join(copy)

for i in instructions:
    if i[0] == 'swap_position':
        string = swap_position(i[1], i[2])
    elif i[0] == 'swap_letter':
        string = swap_letter(i[1], i[2])
    elif i[0] == 'rotate':
        string = rotate(i[1], i[2])
    elif i[0] == 'rotate_position':
        string = rotate_position(i[1])
    elif i[0] == 'reverse':
        string = reverse(i[1], i[2])
    elif i[0] == 'move':
        string = move(i[1], i[2])

print string
