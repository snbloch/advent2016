import io

discs =  []
start_time = 0
capsule_received = False

file = open('input.txt', 'r')
for line in file:
    line = line.strip().split()
    disc = []
    disc.append(int(line[1].replace('#', '')))
    disc.append(int(line[3]))
    disc.append(int(line[11].replace('.', '')))
    discs.append(disc)

while capsule_received == False:
    discs_cleared = []
    time = 0
    for disc in discs:
        time += 1
        if time == disc[0]:
            if (start_time + time + disc[2]) % disc[1] == 0:
                discs_cleared.append(disc)
    if len(discs_cleared) == len(discs):
        capsule_received = True
    else:
        start_time += 1

print start_time
