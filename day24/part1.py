import io
from itertools import permutations

outstanding = []
grid = []
shortest_path = 0

file = open('input.txt', 'r')
for line in file:
    grid.append(line.strip())

def available_moves(curr):
    moves = set()
    for position in curr:
        x = position[0]
        y = position[1]
        if grid[y][x - 1] != '#':
            moves.add((x - 1, y))
        if grid[y][x + 1] != '#':
            moves.add((x + 1, y))
        if grid[y - 1][x] != '#':
            moves.add((x, y - 1))
        if grid[y + 1][x] != '#':
            moves.add((x, y + 1))
    return moves

row_counter = 0
while row_counter < len(grid):
    column_counter = 0
    while column_counter < len(grid[row_counter]):
        if grid[row_counter][column_counter] != '#' and grid[row_counter][column_counter] != '.':
            outstanding.append(grid[row_counter][column_counter])
        if grid[row_counter][column_counter] == '0':
            starting_position = (column_counter, row_counter)
            del outstanding[outstanding.index('0')]
        column_counter += 1
    row_counter += 1

paths = list(permutations(outstanding))
for path in paths:
    num_steps = 0
    head = [starting_position]
    outstanding = list(path)
    while len(outstanding) > 0:
        next_target = outstanding[0]
        num_steps += 1
        if num_steps >= shortest_path and shortest_path != 0:
            break
        head = available_moves(head)
        for position in head:
            if grid[position[1]][position[0]] ==  next_target:
                del outstanding[outstanding.index(next_target)]
                head = [position]
    if shortest_path == 0:
        shortest_path = num_steps
        print 'Shortest path found:', shortest_path
    elif num_steps < shortest_path:
        shortest_path = num_steps
        print 'Shortest path found:', shortest_path

print shortest_path
