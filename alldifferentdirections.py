#alldifferentdirections.py
#open.kattis.com/problems/alldifferentdirections
import io
import sys
import math #math.radians

while True:
    testCases = int(sys.stdin.readline())
    # coordinate_dict = {}
    coordinate_list_x = []
    coordinate_list_y = []


    if testCases!= 0:
        for i in range(testCases):
            input_list = sys.stdin.readline().split(" ")

            startingX = float(input_list.pop(0))
            startingY = float(input_list.pop(0))

            angle_degree = input_list.pop(0)
            angle_degree = float(input_list.pop(0))

            for i in range(len(input_list)//2):
                command = input_list.pop(0)
                value = float(input_list.pop(0))

                if command == "walk":
                    rad_angle = math.radians(angle_degree)
                    # print(rad_angle, type(rad_angle))
                    x_change = math.cos(rad_angle) * value
                    y_change = math.sin(rad_angle) * value
                    # print(x_change, y_change)
                    startingX += x_change
                    startingY += y_change
                    # print("new position", startingX, startingY)

                elif command == "turn":
                    angle_degree = angle_degree + value
            # print("End point", startingX, startingY)
            coordinate_list_x.append(startingX)
            coordinate_list_y.append(startingY)
        
        totalX = sum(coordinate_list_x)
        totalY = sum(coordinate_list_y)

        averageX = totalX / testCases
        averageY = totalY / testCases

        worstDistance = 0

        for i in range(testCases):
            

        print(averageX, averageY)



        
                
    else:
        break