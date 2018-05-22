###########################################################
# Train Passengers
# Gregory Neagu
# May 21, 2018
###########################################################

capacity = 0
stations  = 0
onBoard = 0
run = 1

capacity, stations = input().split(" ")

for i in range(int(stations)):
    line  = input().split(" ")
    gettingOff = int(line[0])
    gettingOn = int(line[1])
    waiting = int(line[2])

    if run == 1:
        if gettingOff != 0:
            print("impossible")
            quit()
    run = 0

    onBoard = onBoard + gettingOn - gettingOff

    if int(onBoard) < 0 or int(onBoard) > int(capacity):
        print("impossible")
        quit()

    if waiting != 0:
        if int(onBoard) < int(capacity):
            print("impossible")
            quit()

if int(onBoard) != 0:
    print("impossible")
    quit()

print("possible")




# capacity = 0
# stations  = 0
# onBoard = 0
#
# capacity, stations = input().split(" ")
#
# for i in range(int(stations)):
#     line  = input().split(" ")
#     gettingOff = int(line[0])
#     gettingOn = int(line[1])
#     waiting = int(line[2])
#
#     onBoard = onBoard + gettingOn - gettingOff
#
#     if int(onBoard) < 0 or int(onBoard) > int(capacity):
#         print("impossible")
#         quit()
#
#     if waiting != 0:
#         if int(onBoard) < int(capacity):
#             print("impossible")
#             quit()
#
# if int(onBoard) != 0:
#     print("impossible")
#     quit()
#
# print("possible")
