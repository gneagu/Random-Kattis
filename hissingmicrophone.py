#############################################################
#
#
#############################################################
import sys
import io

input_string = sys.stdin.readline()
brokenstring = input_string.lower().split("ss")

print(brokenstring)

if (len(brokenstring) >= 2):
    print("hiss")
else:
     print("no hiss")