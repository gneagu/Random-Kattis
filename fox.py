###########################################################
# What does the fox say
# Gregory Neagu
# May 20, 2018
###########################################################
x = int(input())

for i in range(x):
    animalSoundsList = []
    foxSounds = []
    sounds = input().split(" ")
    finalString = ""

    while True:
        line = input()

        if line == "what does the fox say?":
            break

        line = line.split(" ")
        animalSound = line[2]
        animalSoundsList.append(animalSound)

    foxSounds = [item for item in sounds if item not in animalSoundsList]

    for i in foxSounds:
        finalString  = finalString + i + " "

    print(finalString[:-1])
