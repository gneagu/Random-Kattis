#secretmessage
import sys
import io
import math

loops = int(sys.stdin.readline())

# #Initialize array
# for i in range(loops):
#     message = sys.stdin.readline()[:-1]
#     L = int(len(message))
#     M = int(math.ceil(math.sqrt(L)))
#     array = [["*" for u in range(M)] for y in range(M)]
#     pointer = 0

#     for i in range(L, int(math.pow(M, 2))):
#         message+= "*"
    
#     for x in range(0, M)[::-1]:
#         for y in range(0, M):
#             array[x][y] = message[pointer]
#             pointer += 1
    
#     final_message = ""
#     for x in range(0, M):
#         for y in range(0, M):
#             if (array[y][x] != "*"):
#                 final_message += array[y][x]

#     print(final_message)

#Initialize array
for i in range(loops):
    message = sys.stdin.readline()[:-1]
    L = len(message)
    M = int(math.ceil(math.sqrt(L)))
    pointer = 0
    final_message = ""

    for x in range(0, M):
        for y in range(0, M)[::-1]:
            pointer = (y*M) + x
            if (pointer < L):
                final_message += message[pointer]

    print(final_message)