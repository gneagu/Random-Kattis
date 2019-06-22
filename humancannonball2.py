import sys
import io
import math 

num_loop = int(sys.stdin.readline())

for i in range(num_loop):
    input_string = sys.stdin.readline().split(" ")

    v = float(input_string[0])
    ang = float(input_string[1])
    x = float(input_string[2])
    low = float(input_string[3])
    high = float(input_string[4])

    time = x / (v * math.cos(math.radians(ang)))    
    height = (v * time * math.sin(math.radians(ang))) - (0.5 * 9.81 * math.pow(time,2))

    if ((height > low + 1) and (height < high -1)):
        print("safe")
    else:
        print("not safe")
    
    # print(low, height, high, time)