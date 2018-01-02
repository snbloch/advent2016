import io

strings = []
error_corrected = []

file = open('input.txt', 'r')
for line in file:
    strings.append(line.strip())

string_length = len(strings[0])

position = 0
while position < string_length:
    column_string = []
    for string in strings:
        column_string.append(string[position])
    num_occurrences = {}
    for char in column_string:
        num_occurrences[char] = column_string.count(char)
    for char, num in num_occurrences.iteritems():
        if num == max(num_occurrences.values()):
            error_corrected.append(char)
    position += 1

ec_string = ''
for char in error_corrected:
    ec_string += char

print ec_string
