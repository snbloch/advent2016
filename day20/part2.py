import io
from operator import itemgetter

min_int = 0
max_int = 4294967295
num_ports = max_int + 1
max_removed = 0
removals = []

file = open('input.txt', 'r')
for line in file:
    min_to_remove = int(line.split('-')[0])
    max_to_remove = int(line.split('-')[1])
    removals.append((min_to_remove, max_to_remove))

for removal in sorted(removals, key = itemgetter(0)):
    if removal[0] == min_int:
        if removal[1] > max_removed:
            min_int = removal[1] + 1
            num_ports -= removal[1] - removal[0] + 1
            max_removed = removal[1]
    elif removal[0] < min_int:
        if removal[1] > max_removed:
            min_int = removal[1] + 1
            num_ports -= removal[1] - max_removed
            max_removed = removal[1]
    else:
        min_int = removal[1] + 1
        num_ports -= removal[1] - removal[0] + 1
        max_removed = removal[1]

print num_ports
