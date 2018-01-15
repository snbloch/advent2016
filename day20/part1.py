import io
from operator import itemgetter

min_int = 0
max_removed = None
max_int = 4294967295
removals = []

file = open('input.txt', 'r')
for line in file:
    min_to_remove = int(line.split('-')[0])
    max_to_remove = int(line.split('-')[1])
    removals.append((min_to_remove, max_to_remove))

for removal in sorted(removals, key = itemgetter(0)):
    if removal[0] <= min_int:
        if max_removed == None or removal[1] >= max_removed:
            min_int = removal[1] + 1
            max_removed = removal[1]

print min_int
