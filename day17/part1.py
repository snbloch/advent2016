import hashlib
import random

input = 'pxxbnzuo'
min_path = ''
min_path_length = None

def open_doors(input_path):
    open_comparison = 'bcdef'
    doors = []
    hash = hashlib.md5(input_path).hexdigest()[0:4]
    if hash[0] in open_comparison:
        doors.append('U')
    if hash[1] in open_comparison:
        doors.append('D')
    if hash[2] in open_comparison:
        doors.append('L')
    if hash[3] in open_comparison:
        doors.append('R')
    return doors

counter = 0
while counter < 1000000:
    cur_x = 1
    cur_y = 1
    path_taken = ''
    while cur_x != 4 or cur_y != 4:
        next_doors = open_doors(input + path_taken)
        for door in next_doors:
            if cur_x == 1 and 'L' in next_doors:
                next_doors.remove('L')
            if cur_x == 4 and 'R' in next_doors:
                next_doors.remove('R')
            if cur_y == 1 and 'U' in next_doors:
                next_doors.remove('U')
            if cur_y == 4 and 'D' in next_doors:
                next_doors.remove('D')
        if len(next_doors) == 0:
            break
        else:
            next_door = random.choice(next_doors)
            if next_door == 'U':
                cur_y -= 1
            elif next_door == 'D':
                cur_y += 1
            elif next_door == 'L':
                cur_x -= 1
            elif next_door == 'R':
                cur_x += 1
            path_taken += next_door

    if cur_x == 4 and cur_y == 4:
        if min_path_length == None:
            min_path_length = len(path_taken)
            min_path = path_taken
        elif len(path_taken) < min_path_length:
            min_path_length = len(path_taken)
            min_path = path_taken
    counter += 1

print min_path
