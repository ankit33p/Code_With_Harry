"""Exercise 1"""
# Q.CREATE A DICTIOANRY AND TAKE INPUT FROM THE USERS AND RETURN MEANINGS OF THE

dic = {"set": "collection of data",
       "tuples": "immutable",
       "string": "collection of word",
       "int": "numeric value"}
user = input("Enter some words:")
print(dic[user])

"""Exercise-2
Q-Make a faulty calculator, give user input, if the input is 45*3=555,56+9=77,56/6=4,solve all problem correct except these:"""

num1 = int(input("Enter 1st number:"))
num2 = int(input("Enter 2nd number:"))
num3 = input("choose" + "*,+,/,-")
if num1 == 45 and num3 == "*" and num2 == 3:
    print("154")
elif num1 == 56 and num3 == "+" and num2 == 9:
    print("77")
elif num1 == 56 and num3 == "/" and num3 == 6:
    print("4")
elif num3 == "*":
    num4 = num2 * num1
    print(num4)
elif num3 == "+":
    add = num2 + num1
    print(add)
elif num3 == "-":
    sub = num2 - num1
    print(sub)
elif num3 == "/":
    div = num1 / num2
    print(div)
else:
    print("input is wrong ")

"""EXERCISE 3
Q.take input from user tell user that the input no (i) greater than or less than the number given(n).
# no of guesses are limited
# print  as no of guesses left
# print no of guesses taken
# print game over
"""
n = 20
number_of_guesses = 1
print("number_of_guesses limited to : 9")
while number_of_guesses <= 9:
    guess_number = int(input("ENter the number: \n"))
    if guess_number > 20:
        print("Enter a lesser number \n")
    elif guess_number < 20:
        print("Enter a greater number \n")
    else:
        print("you won \n")
        print("number_of_guesses you have taken:", number_of_guesses)
        break
    print(9 - number_of_guesses, "number_of_guesses left")
    number_of_guesses = number_of_guesses + 1
if number_of_guesses > 9:
    print("GAME OVER")

"""EXERCISE 5
manging a health management
"""
# Health Management System
# 3 clients - Harry, Rohan and Hammad

def getdate():
    import datetime
    return datetime.datetime.now()


# Total 6 files
# write a function that when executed takes as input client name
# One more function to retrieve exercise or food for any client


# bhai ye rha program
import datetime


def gettime():
    return datetime.datetime.now()


def take(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("harry-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("harry-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("rohan-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("rohan-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            value = input("type here\n")
            with open("hammad-ex.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
        elif (c == 2):
            value = input("type here\n")
            with open("hammad-food.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("successfully written")
    else:
        print("plz enter valid input (1(harry),2(rohan),3(hammad)")


def retrieve(k):
    if k == 1:
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("harry-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("harry-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 2):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("rohan-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("rohan-food.txt") as op:
                for i in op:
                    print(i, end="")
    elif (k == 3):
        c = int(input("enter 1 for excersise and 2 for food"))
        if (c == 1):
            with open("hammad-ex.txt") as op:
                for i in op:
                    print(i, end="")
        elif (c == 2):
            with open("hammad-food.txt") as op:
                for i in op:
                    print(i, end="")
    else:
        print("plz enter valid input (harry,rohan,hammad)")


print("health management system: ")
a = int(input("Press 1 for log the value and 2 for retrieve "))

if a == 1:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    take(b)
else:
    b = int(input("Press 1 for harry 2 for rohan 3 for hammad "))
    retrieve(b)

"""EXERCISE-6
CREATE a ROCK, Paper, scissor games"""
import random

chance = 10
no_of_chance = 0
x = ['R', 'P', 'S']

pp1 = 0
pp2 = 0

while chance > no_of_chance:
    z = input("Enter P for Paper, R for Rock, S for Scissors:")
    rndom = random.choice(x)

    if z == rndom:
        print(pp1)
        print(pp2)
        print("Both tie")

    elif z == "R" and rndom == "P":
        pp2 = pp2 + 1
        print(f"your guess {z} and computer guess is {rndom} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {pp2} and your point is {pp1} \n ")
    elif z == "R" and rndom == "S":
        pp1 = pp1 + 1
        print(f"your guess {z} and computer guess is {rndom} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {pp2} and your point is {pp1} \n ")

    elif z == "P" and rndom == "S":
        pp2 = pp2 + 1
        print(f"your guess {z} and computer guess is {rndom} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {pp2} and your point is {pp1} \n ")
    elif z == "P" and rndom == "R":
        pp1 = pp1 + 1
        print(f"your guess {z} and computer guess is {rndom} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {pp2} and your point is {pp1} \n ")

    elif z == "S" and rndom == "R":
        pp2 = pp2 + 1
        print(f"your guess {z} and computer guess is {rndom} \n")
        print("computer wins 1 point \n")
        print(f"computer_point is {pp2} and your point is {pp1} \n ")
    elif z == "S" and rndom == "P":
        pp1 = pp1 + 1
        print(f"your guess {z} and computer guess is {rndom} \n")
        print("human wins 1 point \n")
        print(f"computer_point is {pp2} and your point is {pp1} \n ")

    else:
        print("YOU HAVE ENTERED WRONG  INPUT")

    no_of_chance = no_of_chance + 1
    print("no of chance left :", (chance - no_of_chance), "from ", chance)

print("Game Over")
if pp1 == pp2:
    print("THERE IS TIE BETWEEN: HUMAN AND COMPUTER", pp1, "and", pp2)
elif pp1 > pp2:
    print("HUMAN WINS WITH POINTS:", pp1, "which is more by ", (pp1 - pp2))
else:
    print("COMPUTER WINS WITH POINTS:", pp2, "which is more by ", (pp2 - pp1))

print("HUMAN POINT IS :", pp1, "and COMPUTER POINT IS :", pp2)
