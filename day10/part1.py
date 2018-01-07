import io

bots = {}
outputs = {}
instructions = []
found = False
low_target = 17
high_target = 61

file = open('input.txt', 'r')

for line in file:
    #Initial assignments
    if 'value' in line:
        line = line.strip().split()
        if bots.get(line[5]) == None:
            bots[line[5]] = [int(line[1])]
        else:
            bots[line[5]].append(int(line[1]))
    else:
        line = line.strip().split()
        instruction = []
        instruction.append(line[1])
        instruction.append(line[5])
        instruction.append(line[6])
        instruction.append(line[10])
        instruction.append(line[11])
        instructions.append(instruction)

while found == False:
    for instruction in instructions:
        if bots.get(instruction[0]) != None:
            if len(bots[instruction[0]]) == 2:
                low = min(bots[instruction[0]])
                high = max(bots[instruction[0]])
                if low == low_target and high == high_target:
                    found = True
                    print 'Bot',instruction[0],'evaluated',low,'and',high
                    break
                if instruction[1] == 'bot':
                    if bots.get(instruction[2]) == None:
                        bots[instruction[2]] = [low]
                    else:
                        bots[instruction[2]].append(low)
                elif instruction[1] == 'output':
                    if outputs.get(instruction[2]) == None:
                        outputs[instruction[2]] = [low]
                    else:
                        outputs[instruction[2]].append(low)
                if instruction[3] == 'bot':
                    if bots.get(instruction[4]) == None:
                        bots[instruction[4]] = [high]
                    else:
                        bots[instruction[4]].append(high)
                elif instruction[3] == 'output':
                    if outputs.get(instruction[4]) == None:
                        outputs[instruction[4]] = [high]
                    else:
                        outputs[instruction[4]].append(high)
                bots[instruction[0]] = None
            else:
                pass
