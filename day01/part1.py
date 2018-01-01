import io

directions = []
current_x = 0
current_y = 0
current_direction = 'north'

file = open('input.txt', 'r')
for line in file:
    for dir in line.strip().split(', '):
        directions.append((dir[0], int(dir[1:])))

def turn(cur_dir, turn_dir):
    if turn_dir == 'L':
        if cur_dir == 'north':
            return 'west'
        elif cur_dir == 'east':
            return 'north'
        elif cur_dir == 'south':
            return 'east'
        elif cur_dir == 'west':
            return 'south'
    elif turn_dir == 'R':
        if cur_dir == 'north':
            return 'east'
        elif cur_dir == 'east':
            return 'south'
        elif cur_dir == 'south':
            return 'west'
        elif cur_dir == 'west':
            return 'north'

def move(direction, distance):
    global current_x, current_y
    if direction == 'north':
        current_y += distance
    elif direction == 'east':
        current_x += distance
    elif direction == 'south':
        current_y -= distance
    elif direction == 'west':
        current_x -= distance

for dir in directions:
    new_direction = turn(current_direction, dir[0])
    move(new_direction, dir[1])
    current_direction = new_direction

total_distance = abs(current_x) + abs(current_y)
print total_distance
