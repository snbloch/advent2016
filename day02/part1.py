import io
import numpy

keypad_width = 3
keypad_height = 3
moves = []
combination = []

file = open('input.txt', 'r')
for line in file:
    moves.append(line.strip())

def build_keypad(keypad_width, keypad_height):
    keypad = numpy.zeros((keypad_height,keypad_width))
    seed_button = 1
    for y in range(0,keypad_height):
        for x in range(0,keypad_width):
            keypad[y][x] = seed_button
            seed_button += 1
    return keypad

def move_finger(direction, current_x, current_y):
    if direction == 'U' and current_y > 0:
        return current_x, current_y - 1
    elif direction == 'R' and current_x < keypad_width - 1:
        return current_x + 1, current_y
    elif direction == 'D' and current_y < keypad_height - 1:
        return current_x, current_y + 1
    elif direction == 'L' and current_x > 0:
        return current_x - 1, current_y
    else:
        return current_x, current_y

keypad = build_keypad(keypad_width, keypad_height)
current_x = 1
current_y = 1
for button in range(0, len(moves)):
    for move in moves[button]:
        current_x, current_y = move_finger(move, current_x, current_y)
    combination.append(keypad[current_y][current_x])
final_combination = ''
for combo in combination:
    final_combination += str(int(combo))
print final_combination
