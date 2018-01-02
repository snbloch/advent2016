import io
from operator import itemgetter

alpha = 'abcdefghijklmnopqrstuvwxyz'
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
        decrypted_room = ''
        rot = room[1] % 26
        for letter in room[0]:
            initial_position = alpha.index(letter)
            final_position = (initial_position + rot) % 26
            letter = alpha[final_position]
            decrypted_room += letter
        if 'northpole' in decrypted_room:
            print room[1]
