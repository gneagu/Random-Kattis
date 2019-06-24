#cetvrta.oy
import io
import sys

x_axis = {}
y_axis = {}

for i in range(3):
    x,y = sys.stdin.readline().split(" ")
    try:
        x_axis[x] += 1
    except:
        x_axis[x] = 1
    
    try:
        y_axis[y] += 1
    except:
        y_axis[y] = 1

x = 0
y = 0

for i in y_axis:
    if y_axis[i] == 1:
        y = i

for i in x_axis:
    if x_axis[i] == 1:
        x = i

print("{} {}".format(x,y))