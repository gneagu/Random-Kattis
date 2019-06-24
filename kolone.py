#kolone.py

#Second word will not move. Only first will move. 
#haveboth words touch, and offset by 1. (|x|_|x|_|x|x|_|x|)
#Then first word will move. (Just move letters up by x * 2 spaces)
import sys
import io

garbage_collection = sys.stdin.readline()
first_word = list(sys.stdin.readline()[:-1])[::-1]
second_word = list(sys.stdin.readline()[:-1])

letter_list = {}

for i in range(len(first_word), len(first_word) + len(second_word)):
    letter_list[(i * 2) - 1] = second_word[i - len(first_word)]

offset = int(sys.stdin.readline())

for i in range(1, len(first_word) + 1):
    letter_list[((i * 2) - 2) + (offset * 2)] = first_word[i - 1]

final_string = ""

for i in letter_list.values():
    final_string+= i

print(final_string.upper())
