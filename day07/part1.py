import io

ip_addresses = []
tls_supported = 0
abba_found_in_brackets = 0
abba_not_found = 0

file = open('input.txt', 'r')
for line in file:
    ip_addresses.append(line.strip())

for addr in ip_addresses:
    abba_found = False
    abba_fib = False
    in_brackets = False
    addr_length = len(addr)
    position = 0
    while position < len(addr) - 3:
        if in_brackets == False:
            if addr[position] == '[':
                in_brackets = True
                position += 1
            else:
                if addr[position] == addr[position + 3] and addr[position + 1] == addr[position + 2] and addr[position] != addr[position + 1]:
                    abba_found = True
                    abba = addr[position:position + 4]
                position += 1
        if in_brackets == True:
            if addr[position] == ']':
                in_brackets = False
                position += 1
            else:
                if addr[position] == addr[position + 3] and addr[position + 1] == addr[position + 2] and addr[position] != addr[position + 1]:
                    abba_fib = True
                    abba_found_in_brackets += 1
                    break
                else:
                    position += 1
    if abba_found == False and abba_fib == False:
        abba_not_found += 1
        continue
    elif abba_found == True and abba_fib == False:
        tls_supported += 1

print tls_supported
