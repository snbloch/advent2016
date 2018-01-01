import io, sys

directions = []
current_x = 0
current_y = 0
current_direction = 'north'
positions_visited = {}

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
    positions_moved = 0
    global current_x, current_y
    if direction == 'north':
        while positions_moved < distance:
            current_y += 1
            if positions_visited.get(str(current_x) + ',' + str(current_y)) == None:
                positions_visited[str(current_x) + ',' + str(current_y)] = 1
            else:
                positions_visited[str(current_x) + ',' + str(current_y)] += 1
                if positions_visited[str(current_x) + ',' + str(current_y)] == 2:
                    print abs(current_x) + abs(current_y)
                    sys.exit()
            positions_moved += 1
    elif direction == 'east':
        while positions_moved < distance:
            current_x += 1
            if positions_visited.get(str(current_x) + ',' + str(current_y)) == None:
                positions_visited[str(current_x) + ',' + str(current_y)] = 1
            else:
                positions_visited[str(current_x) + ',' + str(current_y)] += 1
                if positions_visited[str(current_x) + ',' + str(current_y)] == 2:
                    print abs(current_x) + abs(current_y)
                    sys.exit()
            positions_moved += 1
    elif direction == 'south':
        while positions_moved < distance:
            current_y -= 1
            if positions_visited.get(str(current_x) + ',' + str(current_y)) == None:
                positions_visited[str(current_x) + ',' + str(current_y)] = 1
            else:
                positions_visited[str(current_x) + ',' + str(current_y)] += 1
                if positions_visited[str(current_x) + ',' + str(current_y)] == 2:
                    print abs(current_x) + abs(current_y)
                    sys.exit()
            positions_moved += 1
    elif direction == 'west':
        while positions_moved < distance:
            current_x -= 1
            if positions_visited.get(str(current_x) + ',' + str(current_y)) == None:
                positions_visited[str(current_x) + ',' + str(current_y)] = 1
            else:
                positions_visited[str(current_x) + ',' + str(current_y)] += 1
                if positions_visited[str(current_x) + ',' + str(current_y)] == 2:
                    print abs(current_x) + abs(current_y)
                    sys.exit()
            positions_moved += 1

for dir in directions:
    new_direction = turn(current_direction, dir[0])
    move(new_direction, dir[1])
    current_direction = new_direction
