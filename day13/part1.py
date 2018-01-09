magic_number = 1358
target_x = 31
target_y = 39
visited = []

def wall_or_open(x, y):
    sum = (x*x + 3*x + 2*x*y + y + y*y) + magic_number
    binary = bin(sum)[2:]
    if binary.count('1') % 2 == 0:
        return 'open'
    else:
        return 'wall'

def choose(locations):
    global visited
    possible = []
    for location in locations:
        x = location[0]
        y = location[1]
        if wall_or_open(x + 1, y) == 'open':
            if (x + 1, y) not in visited:
                possible.append((x + 1, y))
                visited.append((x + 1, y))
        if wall_or_open(x, y + 1) == 'open':
            if (x, y + 1) not in visited:
                possible.append((x, y + 1))
                visited.append((x, y + 1))
        if wall_or_open(x - 1, y) == 'open' and x - 1 >= 0:
            if (x - 1, y) not in visited:
                possible.append((x - 1, y))
                visited.append((x - 1, y))
        if wall_or_open(x, y - 1) == 'open' and y - 1 >= 0:
            if (x, y - 1) not in visited:
                possible.append((x, y - 1))
                visited.append((x, y - 1))
    return possible

current_location = [(1,1)]
destination_reached = False
steps = 0

while destination_reached == False:
    steps += 1
    current_location = choose(current_location)
    if (target_x, target_y) in current_location:
        destination_reached = True

print steps
