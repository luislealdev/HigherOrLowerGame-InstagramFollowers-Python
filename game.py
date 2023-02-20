import random
from art import logo, vs
from data import data

hasLost = False

def getItem():
    return random.choice(data)

def printItem(letter,item):
    print(letter+": "+item["name"]+" | "+item["description"]+" | "+item["country"])

firstItem = getItem()
secondItem = getItem()

print(logo)
while not hasLost:
    print("WHO HAS MORE WOLLOWERS ON INSTAGRAM?")
    print("-----------------")
    printItem("A",firstItem)
    print(vs)
    printItem("B",secondItem)
    print("\n---------------")

    correctInput = False

    while not correctInput:
        answer = input("A or B?").lower()
        if answer=="a":
            correctInput = True
            if(firstItem["follower_count"]>secondItem["follower_count"]):
                print("CORRECT!")
                secondItem=getItem()
            else:
                print("Incorrect :(")
                hasLost=True
        elif answer=="b":
            correctInput = True
            if(firstItem["follower_count"]<secondItem["follower_count"]):
                print("CORRECT!")
                firstItem=secondItem
                secondItem=getItem()
            else:
                print("Incorrect :(")
                hasLost=True
        else:
            print("INCORRECT INPUT, NOT 'A' OR 'B'")