#ferryloading3
#Will first try for one test case, and figure out loop later.
import sys
import io

paramters = sys.stdin.readline().split(" ")
capacity = int(paramters[0])
cross_time = int(paramters[1])
cars_waiting = int(paramters[2])

output_list = list("" for x in range(cars_waiting))
left_list = list()
righ_list = list()

current_time = 0
current_bank = "left"

iterator = 0

print("Cars waiting {}".format(cars_waiting))
print(output_list)


for i in range(cars_waiting):
    output_list[i] = tuple(sys.stdin.readline().split())

    (bank, time) = output_list[i]

    if (bank == "LEFT"):
        left_list.append((i, time))

    if (bank == "RIGHT"):
        righ_list.append((i, time))

    iterator += 1

print(left_list)
print(righ_list)

while ((len(left_list)+ len(righ_list)) > 0):




# for i in range(cars_waiting):
#     output_list[i] = tuple(sys.stdin.readline().split())

# iterator = 0

# while len(output_list) != 0:
#     (bank, time) = output_list[i]

    

#     iterator += 1



# print(output_list)
