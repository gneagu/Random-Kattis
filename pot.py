#pot.py

import sys
import io 
import math

values = int(sys.stdin.readline())

total_value = 0

for i in range(values):
    line = sys.stdin.readline()[:-1]
    num = int(line[:-1])
    power = int(line[-1])
    total_value += int(math.pow(num, power))
    # print("derp", num, power)

print(total_value)