#maptiles2.py
import sys
import io
import math

position = sys.stdin.readline()

print_len = int(len(list(position)[:-1]))
print_x = 0
print_y = 0

for i in range(print_len):
    print_x += ((int(position[i]) % 2) * (math.pow(2, (print_len - (i + 1)))))

for i in range(print_len):
    print_y += (int(position[i]) // 2) * (math.pow(2, print_len - (i + 1)))

print("{} {} {}".format(print_len, int(print_x), int(print_y)))
