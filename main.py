# a looping menu and with responses
import random
import sys


# this wasn't neccesairy but I figured I would leave it in just in case
menuOptions = ["parry", "Dodge", "Swipe", "Stab", "Examine", "Leave"]


menuDialogue = "what will you do?"


# basic printing definition
def showMenu():
    print(menuDialogue)
    menuOptions = ["Parry", "Dodge", "Swipe", "Stab", "Examine", "Leave"]
    for menuOptions in menuOptions:
        message = menuOptions
        print(message)


# for blocking and dodging becuase as of now they don't need unique statements
def defensiveAction():
    print("you " + menuChoice + " their attack!")


# for attacking I added random chance because it was way more interesting
def offensiveAction():
    print("you take a " + menuChoice + " at them!")
    if hitChance == 2:
        print("you missed")
    else:
        print("it hits!")


# I tried to make it as simple as possible with the defined functions
hitChance = random.randint(1, 7)
while True:
    showMenu()
    menuChoice = input("your choice?")
    reRoll = random.randint(1, 5)
    if reRoll == 2:
        hitChance = random.randint(1, 2)
    if menuChoice.lower() == "parry":
        defensiveAction()
    elif menuChoice.lower() == "dodge":
        defensiveAction()
    elif menuChoice.lower() == "swipe":
        offensiveAction()
    elif menuChoice.lower() == "stab":
        offensiveAction()
    elif menuChoice.lower() == "examine":
        print("You Examine the movment of your opponent")
        if hitChance == 2:
            print("you probably won't hit")
        else:
            print("you probably will hit")
    elif menuChoice.lower() == "leave":
        print("you left!")
        sys.exit()
    else:
        print("can't do that, sorry")
