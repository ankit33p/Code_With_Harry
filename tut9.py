#LIST ,TUPELS

grocery=["harpic","rice","rocy","dal","cream","soap",45,54]
print(grocery) #simple print
print(grocery[:])  #print all the list using slicing
print(grocery[4])  #print the element at the index 4

numbers=[1,2,3,4,5,6,7,8,9,0]
print(numbers)  #simple print

print(numbers[2]) #print at index 2

numbers.sort()
print(numbers)#print the list after sorting

numbers.reverse() #print the list after reversing the data
print(numbers)

print(numbers[0:56]) #it print from 0 to till last because it just ignore the exceeded range.

print(numbers[:]) #simply print all the list

print(numbers[::]) #print all the list

print(numbers[:8])  #print the list from range of 0 to 7 because the last index input is excluded.

print(numbers[4:])  #print the list from range of 4 to till last.

"""the no of index is given at place of 6 it skip that number of index"""
print(numbers[0:10:6])

print(numbers[-6:-1])  # print from the end start from -6 to -1 (i.e is last).

print(numbers[: :-2])  # print oppositely and skip 1 index.

print(numbers[: :-1])  # print oppositely

"""IN NEGATIVE SLICING IN LIST DONT TAKE THE VALUE LESS THAN -1"""

print(max(numbers))  #print the maximum numbers

print(min(numbers))  #print the minimum numbers

numbers.append(54)  #to add numbers at last
print(numbers)

numbers.insert(2,34)  #to add numbers in list at specified position
print(numbers)

numbers.remove(4) #to remove the number from the lists
print(numbers)

numbers.pop()  #to pop out the last number from the list
print(numbers)

"""TUPLES:-it is immutable i.e data cannot be changed."""

tp=(1,32,4,5,)  #Enter data as tuples.
print(tp)

#tp[1]=5 #shows an eror bcoz tuples are immutable
#print(tp)

"""If we want to add only one item in tuples we have to give a (,) like (2,)"""
tp=(1,)
print(tp)

"""SWAPPING THE DATA"""
a=4
b=10
a,b=b,a
print(a,b)