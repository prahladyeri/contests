coord1_x, coord1_y = input().split()
coord2_x, coord2_y = input().split()
coord3_x, coord3_y = input().split()
coord4_x, coord4_y = 0, 0

coord1_x, coord1_y = int(coord1_x), int(coord1_y)
coord2_x, coord2_y = int(coord2_x), int(coord2_y)
coord3_x, coord3_y = int(coord3_x), int(coord3_y)

if coord1_x == coord2_x or coord1_x==coord3_x:
    if coord1_x == coord2_x:
           coord4_x=coord3_x
    else:
           coord4_x=coord2_x
else:
    coord4_x=coord1_x
if coord1_y == coord2_y or coord1_y==coord3_y:
    if coord1_y == coord2_y:
           coord4_y=coord3_y
    else:
           coord4_y=coord2_y
else:
    coord4_y=coord1_y

print(coord4_x, coord4_y)
