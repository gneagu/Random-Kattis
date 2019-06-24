#drmmessages.py
import io
import sys

input_string = sys.stdin.readline().lower()
length = len(input_string[:-1])
half_point = int(length /2)
first_half = input_string[0:half_point]
last_half = input_string[half_point:length]

letter_mapping = {}
reverse_mapping = {}

iterator = 0

for i in range(97,123):
    letter_mapping[chr(i)] = iterator
    reverse_mapping[iterator] = chr(i)
    iterator += 1

x = 0
y = 0
for i in first_half:
    x = x + letter_mapping[i]

for i in last_half:
    y = y + letter_mapping[i]

new_first_half = ""
for i in first_half:
    new_first_half += (reverse_mapping[(letter_mapping[i] + x ) % 26])

new_last_half = ""
for i in last_half:
    new_last_half += (reverse_mapping[(letter_mapping[i] + y ) % 26])

final_output = ""

for i in range(len(new_first_half)):
    final_output += reverse_mapping[(letter_mapping[new_first_half[i]] + letter_mapping[new_last_half[i]]) % 26]

print(final_output.upper())