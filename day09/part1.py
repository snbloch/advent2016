import io

position = 0
output_string = ''

file = open('input.txt', 'r')
input_string = file.read().strip()

def get_expansion(position):
    start = int(input_string.find('(', position))
    end = int(input_string.find(')', position))
    return start, end

expansion_start, expansion_end = get_expansion(position)
while expansion_start != -1:
    if position != expansion_start:
        output_string += input_string[position:expansion_start]
        position = expansion_start
    else:
        num_chars = int(input_string[expansion_start + 1:expansion_end].split('x')[0])
        repeat = int(input_string[expansion_start + 1:expansion_end].split('x')[1])
        expanded_string = input_string[expansion_end + 1:expansion_end + 1 + num_chars] * repeat
        output_string += expanded_string
        position = expansion_end + 1 + num_chars
        expansion_start, expansion_end = get_expansion(position)
output_string += input_string[position:len(input_string)]

print len(output_string)
