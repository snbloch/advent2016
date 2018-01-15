num_elves = 3012210
binary = str(bin(num_elves))[2:]
binary = binary[1:] + binary[0]
solution = int(binary, 2)
print solution
