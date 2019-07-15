#mjehuric.py

import io
import sys

list_of_values = sys.stdin.readline()[:-1].split(" ")

comparative_final = sorted(list_of_values)

if list_of_values == comparative_final:
    print("{} {} {} {} {}".format(list_of_values[0], list_of_values[1], list_of_values[2], list_of_values[3], list_of_values[4]))

while (list_of_values != comparative_final):

    for i in range(len(comparative_final[:-1])):
        if list_of_values[i] > list_of_values[i + 1]:
            temp_value = list_of_values[i]
            list_of_values[i] = list_of_values[i + 1]
            list_of_values[i + 1] = temp_value
            print("{} {} {} {} {}".format(list_of_values[0], list_of_values[1], list_of_values[2], list_of_values[3], list_of_values[4]))
  

    