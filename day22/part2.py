import io

nodes = []
viable_pairs = 0
max_x = 0
max_y = 0
step_counter = 0
target_location = (0, 0)

file = open('input.txt', 'r')
for line in file:
    if 'df -h' in line:
        pass
    elif 'Filesystem' in line:
        pass
    else:
        node = []
        line = line.strip().split()
        x = int(line[0].split('-')[1].replace('x', ''))
        y = int(line[0].split('-')[2].replace('y', ''))
        size = int(line[1].replace('T', ''))
        used = int(line[2].replace('T', ''))
        avail = int(line[3].replace('T', ''))
        node.append((x, y))
        node.append(size)
        node.append(used)
        node.append(avail)
        nodes.append(node)

def find_empty():
    for node in nodes:
        if node[2] == 0:
            return node

for node in nodes:
    if node[0][0] > max_x and node[0][1] == 0:
        max_x = node[0][0]
    if node[0][1] > max_y and node[0][0] == 0:
        max_y = node[0][1]

empty_node = find_empty()
grid = []
y_counter = 0
while y_counter <= max_y:
    row = []
    x_counter = 0
    while x_counter <= max_x:
        for node in nodes:
            if node[0] == (x_counter, y_counter):
                if node[0] == empty_node[0]:
                    row.append('_')
                elif x_counter == max_x and y_counter == 0:
                    row.append('G')
                elif float(node[2]) / float(node[1]) * 100 > 95:
                    row.append('#')
                else:
                    row.append('.')
        x_counter += 1
    grid.append(row)
    y_counter += 1

for row in grid:
    print ''.join(row)
