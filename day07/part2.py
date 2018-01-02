import io

ip_addresses = []
ssl_supported = 0
bab_count = 0

file = open('input.txt', 'r')
for line in file:
    ip_addresses.append(line.strip())

for addr in ip_addresses:
    aba = ''
    bab = ''
    aba_found = False
    bab_found = False
    in_brackets = False
    addr_length = len(addr)
    position = 0
    bracket_position = 0
    strings_in_brackets = []
    while True:
        string_start = addr.find('[', bracket_position)
        string_end = addr.find(']', bracket_position)
        if string_start == -1:
            break
        strings_in_brackets.append(addr[string_start + 1:string_end])
        bracket_position = string_end + 1
    while position < len(addr) - 2:
        if in_brackets == False:
            if addr[position] == '[':
                in_brackets = True
                position += 1
            else:
                if addr[position] == addr[position + 2] and addr[position + 1] != addr[position]:
                    aba_found = True
                    aba = addr[position:position + 3]
                    bab = addr[position + 1] + addr[position] + addr[position + 1]
                    for string in strings_in_brackets:
                        if bab in string:
                            bab_found = True
                position += 1
        if in_brackets == True:
            if addr[position] == ']':
                in_brackets = False
                position += 1
            else:
                position += 1
    if aba_found == True and bab_found == True:
        ssl_supported += 1

print ssl_supported
