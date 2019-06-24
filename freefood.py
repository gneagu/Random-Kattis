#freefood
import sys
import io

iterations = int(sys.stdin.readline())
date_list = {}

for i in range(iterations):
    start, end = sys.stdin.readline().split(" ")

    if start == end:
        date_list[start] = 1
    else:
        for i in range(int(start), int(end) + 1):
            date_list[i] = 1

print(len(date_list))