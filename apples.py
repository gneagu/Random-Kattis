###########################################################
# What does the fox say
# Gregory Neagu
# May 26, 2018
###########################################################
import sys

R,C = sys.stdin.readline().split(" ")
graph= {}

R = int(R)
C = int(C)

for r in range(R):
    line = sys.stdin.readline()

    for c in range(C):
        try:
            graph[c].append(line[c])
        except:
            graph[c] = [line[c]]

# print(graph)

for c in range(C):
    blockade = R
    currentPoint = 0

    #  Retry in C++
    # for r in range(R):
    #     if graph[c][r] == '#':
    #         blockade = r
    #     elif graph[c][r] == 'a':
    #         tempPointer = graph[c][blockade - 1]*
    #         graph[c][blockade - 1]* = graph[c][r]*
    #         graph[c][r]* = tempPointer
    #         tempPointer = 0
    #         blockade -= 1

    for r in range(R - 1, -1, -1):
        if graph[c][r] == '#':
            blockade = r
        elif graph[c][r] == 'a':
            tempVal = graph[c][blockade - 1]
            graph[c][blockade - 1] = graph[c][r]
            graph[c][r] = tempVal
            tempPointer = 0
            blockade -= 1

for r in range(R):
    line = ""

    for c in range(C):
        line += graph[c][r]

    print(line)
