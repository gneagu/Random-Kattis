###########################################################
# Train Passengers
# Gregory Neagu
# May 21, 2018
###########################################################
import sys

totalInput = ""
totalInput = sys.stdin.readlines()

for line in totalInput:
    x = len(line)
    i = 0
    hexDigit = ""

    while i < x:

        if line[i] == "0":
            i = i + 1

            if line[i] == 'x' or line[i] == 'X':
                currentPlace = 0
                totalInput = '0' + line[i]
                i += 1
                currentI = i

                while currentPlace < 8:
                    actualPlace = currentI + currentPlace

                    if (line[actualPlace] >= 'a' and line[actualPlace] <= 'f') \
                    or (line[actualPlace] >= 'A' and line[actualPlace] <= 'F') \
                    or (line[actualPlace] >= '0' and line[actualPlace] <= '9') :
                        totalInput += line[actualPlace]
                        currentPlace += 1
                        i += 1
                    else:
                        i += 1
                        break

            print( "{} {}".format(totalInput, int(totalInput, 16)))
        else:
            i = i + 1
