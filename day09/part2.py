import io

position = 0
output_string_length = 0

file = open('input.txt', 'r')
input_string = file.read().strip()

def repeat_string(repeat, string):
    return expand(string) * repeat

def get_expansion(position, string):
    start = int(string.find('(', position))
    end = int(string.find(')', position))
    return start, end

def expand(string):
    start, end = get_expansion(0, string)
    position = 0
    if start == -1 and end == -1:
        return string
    else:
        if position != start:
            intermediate_string = string[0:start] + expand(string[start:])
        else:
            num_chars = int(string[start + 1:end].split('x')[0])
            repeat = int(string[start + 1:end].split('x')[1])
            intermediate_string = repeat_string(repeat, string[end + 1:end + 1 + num_chars]) + expand(string[end + 1 + num_chars:])
            #print intermediate_string
    return intermediate_string

expansion_start, expansion_end = get_expansion(position, input_string)
while expansion_start != -1:
    if position != expansion_start:
        output_string_length += len(input_string[position:expansion_start])
        position = expansion_start
    else:
        num_chars = int(input_string[expansion_start + 1:expansion_end].split('x')[0])
        output_string_length += len(expand(input_string[expansion_start:expansion_end + 1 + num_chars]))
        position = expansion_end + 1 + num_chars
        expansion_start, expansion_end = get_expansion(position, input_string)
output_string_length += len(input_string[position:len(input_string)])

print output_string_length
