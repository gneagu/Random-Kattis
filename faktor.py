import sys
import io
input_string = sys.stdin.readline()
seperated_string = input_string.split(" ")

a = int(seperated_string[0])
b = int(seperated_string[1])

c = (a * (b - 1)) + 1

print(c)