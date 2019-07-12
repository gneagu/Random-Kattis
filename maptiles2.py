#maptiles2.py
import sys
import io
import math

#Essentially, get tile number. (Which just tells us
# the quardrant). So, based on num of letters, 
# can know zoom. 

# Based on zoom,go backwards 
# Ex// xyz - zoom 3 (3 numbers)
# x^3, y^2, y^1. (can use to find quadrants)

#2 ^ zoom = 8 (8 // 2) * x + ( )
# ex// x_cord = 2 ^ (zoom - x)

# 2 ^ zoom = full
# ((full // 2) * (x % 2) + (((full /2)// 2) * (y %2) +
#  ((full/2/2 // 2) * (z%2)) = x position

# For X % 2
# idea being that mod x by 2 (Either 0 or 1) meaning 
# left or right.
# So by x,y,z,... Can do (num %2) * (2 ^ (zoom - pos))
# For all values, and this should give X. 

# For Y // 2
# ((x // 2) * (2 ^ (zoom - pos))) +
# ((y // 2) * (2 ^ (zoom - pos))) + 
# ((z // 2) * (2 ^ (zoom - pos)))

# Ex// 3 
# zoom = len(3) = 1
#X = 1
# (3 % 2) * ( 2 ^ (1 - 1)) = 1
#Y = 1
# (3 // 2) * (2 ^ (1 - 1)) = 1

# Ex// 130
# zoom = len(130) = 3
#X = 6
# (1 % 2) * (2 ^ (3 - 1)) = (1 * 2 ^ 2) = 4
# (3 % 2) * (2 ^ (3 - 2)) = (1 * 2 * 1) = 2
# (0 % 2) * (2 ^ (3 - 3)) = (0 * 2 ^ 0) = 0
#Y = 2
# (1 //2) * (2 ^ (3 - 1)) = (0 * 2 ^ 2) = 0
# (3 //2) * (2 ^ (3 - 2)) = (1 * 2 ^ 1) = 2
# (0 //2) * (2 ^ (3 - 3)) = (0 * 2 ^ 0) = 0

position = sys.stdin.readline()

print_len = int(len(list(position)[:-1]))
print_x = 0
print_y = 0

x = 0 

for i in range(print_len):
    print_x += ((int(position[x]) % 2) * (math.pow(2, (print_len - (x + 1)))))
    # # print(print_x, position[x], int(position[x]) % 2), (2 ^ (print_len - x + 1))
    # print("part 1", int(position[x]) % 2)
    # print("part 2", (math.pow(2, (print_len - (x + 1)))))
    x += 1
print(int(print_x))

x = 0

for i in range(print_len):

    print_y += (int(position[x]) // 2) * (math.pow(2, print_len - (x + 1)))
    # print("{}".format(int(position[x]) // 2))
    # print("{}".format(math.pow(2, print_len - (x + 1))))
    # print("{}".format(int(int(position[x]) % 2) * (math.pow(2, print_len - x + 1))))
    # print(print_y, position[x], int(position[x]) // 2), (math.pow((print_len - x + 1),2), x)
    x += 1

print(int(print_y))

print(print_len, print_x, print_y)
