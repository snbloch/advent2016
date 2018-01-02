import io
from operator import itemgetter

rooms = []
sector_id_sum = 0

file = open('input.txt', 'r')
for line in file:
    line = line.strip()
    checksum_start = line.index('[')
    checksum_end = line.index(']')
    checksum = line[checksum_start + 1:checksum_end]
    line = line.replace('[' + checksum + ']', '')
    sector_id = line.split('-')[-1]
    name_length = len(line.split('-')) - 1
    name = ''
    for string in line.split('-')[0:name_length]:
        name += string
    rooms.append([name, int(sector_id), checksum])

for room in rooms:
    char_count = {}
    for char in room[0]:
        char_count[char] = room[0].count(char)
    char_count = sorted(sorted(char_count.items(), key=itemgetter(0)), key=itemgetter(1), reverse=True)
    position = 0
    checksum = ''
    while position < 5:
        checksum += char_count[position][0]
        position += 1
    if checksum == room[2]:
        sector_id_sum += room[1]

print sector_id_sum
