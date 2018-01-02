import io
import numpy

keypad_width = 5
keypad_height = 5
moves = []
combination = []

file = open('input.txt', 'r')
for line in file:
    moves.append(line.strip())

def build_keypad(keypad_width, keypad_height):
    keypad = numpy.zeros((keypad_height,keypad_width))
    keypad[0][2] = ord('1')
    keypad[1][1] = ord('2')
    keypad[1][2] = ord('3')
    keypad[1][3] = ord('4')
    keypad[2][0] = ord('5')
    keypad[2][1] = ord('6')
    keypad[2][2] = ord('7')
    keypad[2][3] = ord('8')
    keypad[2][4] = ord('9')
    keypad[3][1] = ord('A')
    keypad[3][2] = ord('B')
    keypad[3][3] = ord('C')
    keypad[4][2] = ord('D')
    return keypad

def move_finger(direction, current_x, current_y):
    if direction == 'U' and current_y > 0 and keypad[current_y - 1][current_x] != 0:
        return current_x, current_y - 1
    elif direction == 'R' and current_x < keypad_width - 1 and keypad[current_y][current_x + 1] != 0:
        return current_x + 1, current_y
    elif direction == 'D' and current_y < keypad_height - 1 and keypad[current_y + 1][current_x] != 0:
        return current_x, current_y + 1
    elif direction == 'L' and current_x > 0 and keypad[current_y][current_x - 1] != 0:
        return current_x - 1, current_y
    else:
        return current_x, current_y

keypad = build_keypad(keypad_width, keypad_height)

current_x = 0
current_y = 2
for button in range(0, len(moves)):
    for move in moves[button]:
        current_x, current_y = move_finger(move, current_x, current_y)
    combination.append(keypad[current_y][current_x])
final_combination = ''
for combo in combination:
    final_combination += chr(int(combo))
print final_combination
