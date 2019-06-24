#alldifferentdirections.py
#open.kattis.com/problems/alldifferentdirections
import io
import sys
import math #math.radians

while True:
    testCases = int(sys.stdin.readline())
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
                    x_change = math.cos(rad_angle) * value
                    y_change = math.sin(rad_angle) * value
                    startingX += x_change
                    startingY += y_change
                elif command == "turn":
                    angle_degree = angle_degree + value

            coordinate_list_x.append(startingX)
            coordinate_list_y.append(startingY)
        
        totalX = sum(coordinate_list_x)
        totalY = sum(coordinate_list_y)
        averageX = totalX / testCases
        averageY = totalY / testCases
        worstDistance = 0

        for i in range(testCases):
            distance = math.sqrt(pow(coordinate_list_x[i] - averageX,2) + pow(coordinate_list_y[i] - averageY,2))
            if worstDistance < distance:
                worstDistance = distance

        print(averageX, averageY, worstDistance)
                    
    else:
        break