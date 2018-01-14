input = '11100010111110100'
target_length = 272

while len(input) < target_length:
    copy = ''
    position = len(input) - 1
    while position >= 0:
        if input[position] == '0':
            copy += '1'
        else:
            copy += '0'
        position -= 1
    input = input + '0' + copy

input_for_checksum = input[0:target_length]
checksum_found = False
checksum = ''
position = 0
while position < target_length:
    if input[position] == input[position + 1]:
        checksum += '1'
    else:
        checksum += '0'
    position += 2
if len(checksum) % 2 != 0:
    checksum_found = True
    print checksum

while checksum_found == False:
    temp_checksum = ''
    position = 0
    while position < len(checksum):
        if checksum[position] == checksum[position + 1]:
            temp_checksum += '1'
        else:
            temp_checksum += '0'
        position += 2
    checksum = temp_checksum
    if len(checksum) %2 != 0:
        checksum_found = True
        print checksum
