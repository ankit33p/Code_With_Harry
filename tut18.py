"""BREAK AND CONTINUE"""

# if we want to print from 1 to 45;
i = 0
while (i < 45):  # it will print from 1 to 45
    print(i+1)
    i=i+1

# if we wan tout print in one line
i = 0
while (i < 45):  # it will print from 1 to 45
    print(i+1,end=" ")
    i=i+1


# NOTE:-if we use while(1) and while (True) it run infinitely until we dont stop it
# i = 0
# while(1):
#   print(i+1)

# break- to stop a loop we use BREAK statement
i = 0
while (True):  # it will print from 1 to 45
    print(i+1)
    if i==44:
        break
    i=i+1
# using of break and continue
i = 0
while (True): # it will print from 1 to 45
    if i+1 < 5:
        i=i+1
        continue
    print(i+1,end="\n")
    if i==44:
        i=i+1
        break
    i=i+1

"""NOTE-
break- USE TO DESTROY THE LOOP
continue- USE TO FORGET AFTER THE CURRENT ITERATIONS"""


