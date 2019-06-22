import io
import sys

string_input = sys.stdin.readline()
split_input = string_input.split(" ")

val_king = 1 - int(split_input[0])
val_queen = 1 - int(split_input[1])
val_rooks = 2 - int(split_input[2])
val_bishop = 2 - int(split_input[3])
val_knight = 2 - int(split_input[4])
val_pawn = 8 - int(split_input[5])

outputString = "{} {} {} {} {} {}".format(val_king, val_queen, val_rooks, \
    val_bishop, val_knight, val_pawn)

print(outputString)