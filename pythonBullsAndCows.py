# The game bulls and cows

colors = ['r','o','y','g','b','p']
from itertools import permutations
options = list(permutations(colors,4))
from random import randint

# Guessing the player's colors
def guess():
    repeat = 0
    rightPositions = 0
    options1 = options.copy()
    while rightPositions < 4:
        myGuess = options1[randint(0,len(options1) - 1)]
        print(myGuess)
        repeat = repeat + 1
        rightColors = int(input("How much right colors? "))
        rightPositions = int(input("How much right positions? "))
        options1 = sort(rightColors,rightPositions,myGuess,options1)
    print("took me ", repeat, " guesses")
    main()

# sorting the options
def sort(rightColors,rightPositions,myGuess,options1): #FILL THIS FUNCTION
    wrong = set()
    for option in options1:
        if sameColor(option, myGuess) != rightColors:
            wrong.add(option)
        elif samePosition(option, myGuess) != rightPositions:
            wrong.add(option)
    return list(set(options1) - wrong)

# Choosing colors and checking the player's guesses
def choose():
    repeat = 0
    right = list(options[randint(0,len(options))])
    #print(right)
    found = False
    while not(found):
        repeat = repeat + 1
        a = input("first color \n")
        b = input("second color \n")
        c = input("third color \n")
        d = input("fourth color \n")
        currentGuess = [a,b,c,d]
        if currentGuess == right:
            print("right, took you ",repeat, " guesses")
            found = True
        else:
            check(currentGuess,right)
    main()

# checking the guess
def check(currentGuess, right):
    print(sameColor(currentGuess,right), " right colors")
    print(samePosition(currentGuess,right), " right positions")

# returning the number of similar colors between 2 options
def sameColor(option1, option2):
    different = set(option2) - set(option1)
    return 4 - len(different)

# returning the number of similar positions between 2 options
def samePosition(option1, option2):
    same = 0
    for num in range(4):
        if option1[num] == option2[num]:
            same = same + 1
    return same

# The game
def main():
    setting = int(input("who chooses the colors first? \n You - 1 \n The computer - 2 \n Stop playing - 3 \n"))
    if setting == 1:
        guess()
    elif setting == 2:
        choose()
    else:
        quit()

print("The colors are red, orange, yellow, green, blue, purple. \n Use the first letter of each color. \n Each color can appear only one time.")
main()