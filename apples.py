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

print("")

for r in range(R):
    # print("R", R, "C", C)
    line = sys.stdin.readline()

    for c in range(C):
        try:
            graph[c].append(line[c])
        except:
            graph[c] = [line[c]]

print(graph)

for c in range(C):
    # print( "C")
    blockade = R
    currentPoint = 0

    #  Retry in C++
    # for r in range(R):
    #     if graph[c][r] == '#':
    #         blockade = r
    #     elif graph[c][r] == 'a':
    #         tempPointer = graph[c][blockade + 1]*
    #         graph[c][blockade + 1]* = graph[c][r]*
    #         graph[c][r]* = tempPointer
    #         tempPointer = 0

    for r in range(R - 1, -1, -1):
        print(c, r)
        if graph[c][r] == '#':
            blockade = r
        elif graph[c][r] == 'a':
            # currentPoint = c
            tempVal = graph[c][blockade - 1]
            graph[c][blockade - 1] = graph[c][r]
            graph[c][r] = tempVal
            tempPointer = 0

#S







print(graph)
