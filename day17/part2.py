import hashlib
from collections import deque

input = 'pxxbnzuo'
max_path_length = 0
head = deque()

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

start_x = 1
start_y = 1
head.append([(start_x, start_y), input])
while len(head) > 0:
    current_position, hash = head.popleft()
    if current_position[0] == 4 and current_position[1] == 4:
        if len(hash[8:]) >  max_path_length:
            max_path_length = len(hash[8:])
        continue
    for door in open_doors(hash):
        if door == 'L' and current_position[0] > 1:
            next_position = (current_position[0] - 1, current_position[1])
            head.append([next_position, hash + 'L'])
        if door == 'R' and current_position[0] < 4:
            next_position = (current_position[0] + 1, current_position[1])
            head.append([next_position, hash + 'R'])
        if door == 'U' and current_position[1] > 1:
            next_position = (current_position[0], current_position[1] - 1)
            head.append([next_position, hash + 'U'])
        if door == 'D' and current_position[1] < 4:
            next_position = (current_position[0], current_position[1] + 1)
            head.append([next_position, hash + 'D'])

print max_path_length
