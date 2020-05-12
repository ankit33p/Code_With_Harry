"""SET:set is a collection of well defined object"""

s=set()
print(type(s))  # to k ow the datatype

l=[1,2,3,45,6]
s=set(l) #s_from_list
print(s)  #to print the set using list
print(type(s))

"""if we add another 1 in the set we get only one 1 becuase set consist of  unique elements."""
s.add(1)
print(s)  # to add in the set

"""UNION OF SET"""
s1=s.union({1,2,3,4,5,6})  #what we add its just take union of it and the another input
print(s,s1)


"""INTERSECTION OF SETS"""
s1=s.intersection({1,2,3,4,5,6,3,4,5,768765,432})
print(s,s1)
print(len(s))
print(max(s))
print(min(s))
print(s1.isdisjoint(s))   #to know whether s and s1 is disjoint or not(True,False)


s.remove(45)  #to remove from the set
print(s)


