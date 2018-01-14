import io
from numpy import zeros, count_nonzero

file = open('input.txt', 'r')
line = file.readline().strip()

row_count = 400000
column_count = len(line)
grid = zeros((row_count, column_count))

def determine_safety(row_position, column_position):
    left_safe = False
    center_safe = False
    right_safe = False
    if column_position == 0:
        left_safe = True
    else:
        if grid[row_position - 1][column_position - 1] == 0:
            left_safe = True
    if column_position == column_count - 1:
        right_safe = True
    else:
        if grid[row_position - 1][column_position + 1] == 0:
            right_safe = True
    if grid[row_position - 1][column_position] == 0:
        center_safe = True
    if left_safe == False and center_safe == False and right_safe == True:
        return False
    if center_safe == False and right_safe == False and left_safe == True:
        return False
    if left_safe == False and center_safe == True and right_safe == True:
        return False
    if left_safe == True and center_safe == True and right_safe == False:
        return False
    return True


position = 0
for char in line:
    if char == '^':
        grid[0][position] = 1
    position += 1

row_position = 1
while row_position < row_count:
    column_position = 0
    while column_position < column_count:
        if determine_safety(row_position, column_position) == False:
            grid[row_position][column_position] = 1
        column_position += 1
    row_position += 1

print grid.size - count_nonzero(grid)
