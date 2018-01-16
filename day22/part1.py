import io

nodes = []
viable_pairs = 0

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

for node in nodes:
    if node[2] == 0:
        continue
    for comparison_node in nodes:
        if comparison_node[0] == node[0]:
            continue
        else:
            if node[2] <= comparison_node[3]:
                viable_pairs += 1

print viable_pairs
