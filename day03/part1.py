import io

potential_triangles = []
valid_triangles = 0

file = open('input.txt', 'r')
for line in file:
    tri = []
    line = line.strip()
    for side in line.split():
        tri.append(int(side))
    potential_triangles.append(tri)

def is_triangle_valid(side1, side2, side3):
    if side1 + side2 > side3:
        return True
    else:
        return False

for tri in potential_triangles:
    tri = sorted(tri)
    if is_triangle_valid(tri[0], tri[1], tri[2]):
        valid_triangles += 1

print valid_triangles
