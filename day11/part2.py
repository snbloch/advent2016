from itertools import combinations

states = []
steps = 0

def possible_floors(cur_floor):
    if cur_floor == 0:
        return [1]
    elif cur_floor == 1:
        return [0, 2]
    elif cur_floor == 2:
        return [1, 3]
    elif cur_floor == 3:
        return [2]

def next_states(states):
    global observed_states
    possible_states = []
    for state in states:
        cur_floor = state[0]
        cur_layout = state[1]
        next_floors = possible_floors(cur_floor)
        if len(cur_layout[0]) == 0 and 0 in next_floors:
            next_floors.remove(0)
        if len(cur_layout[0]) == 0 and len(cur_layout[1]) == 0 and 1 in next_floors:
            next_floors.remove(1)
        item_counts = []
        for floor in next_floors:
            items = []
            for item in combinations(cur_layout[cur_floor][1], 2):
                items.append(item)
            for item in cur_layout[cur_floor][1]:
                items.append(item)
            for item in items:
                new_layout = []
                floor_counter = 0
                for existing_floor in cur_layout:
                    if floor_counter != cur_floor and floor_counter != floor:
                        new_layout.append(existing_floor)
                    elif floor_counter == cur_floor:
                        existing_floor = list(existing_floor)
                        existing_floor_items = list(existing_floor[1])
                        if type(item) == tuple:
                            for i in item:
                                existing_floor_items.remove(i)
                        else:
                            existing_floor_items.remove(item)
                        existing_floor = tuple((floor_counter, tuple(existing_floor_items)))
                        new_layout.append(existing_floor)
                    elif floor_counter == floor:
                        existing_floor = list(existing_floor)
                        existing_floor_items = list(existing_floor[1])
                        if type(item) == tuple:
                            for i in item:
                                existing_floor_items.append(i)
                        else:
                            existing_floor_items.append(item)
                        existing_floor = tuple((floor_counter, tuple(existing_floor_items)))
                        new_layout.append(existing_floor)
                    floor_counter += 1
                floor_counter = 0
                for f in new_layout:
                    if type(f[1]) == list:
                        f_copy = list(f)
                        new_layout.remove(f)
                        to_tuple = f_copy[1]
                        f_copy.remove(to_tuple)
                        f_copy.append(tuple(to_tuple))
                        new_layout.insert(floor_counter, tuple(f_copy))
                    floor_counter += 1
                new_layout = tuple(new_layout)
                bad_layout = False
                for test_floor in new_layout:
                    microchips = ''
                    generators = ''
                    microchip_count = 0
                    generator_count = 0
                    for item in test_floor[1]:
                        if item[1] == 'M':
                            microchips += item[0]
                            microchip_count += 1
                        elif item[1] == 'G':
                            generators += item[0]
                            generator_count += 1
                    if generator_count > 0:
                        if microchip_count > generator_count:
                            bad_layout = True
                            break
                        elif microchip_count > 0:
                            for chip in microchips:
                                if chip not in generators:
                                    bad_layout = True
                                    break
                    item_counts.append((microchip_count, generator_count))
                if bad_layout == False:
                    item_counts_tuple = tuple(item_counts)
                    if hash(((floor, item_counts_tuple))) in observed_states:
                        pass
                    else:
                        possible_states.append((floor, new_layout))
                        observed_states.append(hash((floor, item_counts_tuple)))
    return possible_states

observed_states = []
floors = []
elevator_location = 0
floors.append((0, ('SG', 'SM', 'PG', 'PM', 'EM', 'EG', 'DM', 'DG')))
floors.append((1, ('TG', 'RG', 'RM', 'CG', 'CM')))
floors.append((2, ('TM',)))
floors.append((3, ()))
item_counts = []
for floor in floors:
    microchips_count = 0
    generators_count = 0
    for item in floor[1]:
        if item[1]== 'M':
            microchips_count += 1
        elif item[1] == 'G':
            generators_count += 1
    item_counts.append((microchips_count, generators_count))
states.append((elevator_location, floors))
observed_states.append((elevator_location, item_counts))
game_over = False

while game_over == False:
    steps += 1
    print 'Starting step',steps
    states = next_states(states)
    for state in states:
        if len(state[1][0][1]) == 0 and len(state[1][1][1]) == 0 and len(state[1][2][1]) == 0:
            game_over = True
print 'Total steps:',steps
