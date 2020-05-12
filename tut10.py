"""DICTIONARY"""
#dictionary is nothing but key value pairs.

d1={}
print(type(d1))  #to know the type

d2={"prince":"chicken","rgahav":"meat","nisha":"love"}
print(d2)  #to print the value of dict
print(d2["prince"])  #to print a exact value

"""We can input a dictionary in a dictionary"""
d2={"prince":"chicken","rgahav":"meat","nisha":"love","raj":{"B":"maggie","L":"rice","D":"juice"}}
print(d2)
print(d2["raj"])
print(d2["raj"]["B"])  #to print internal dict specified items

"""Dictionary values can be any data types like int, strings,dict,list and tuples  only keys are immutable"""

d2["nishant"]="ramu" #to add some items
print(d2)

del d2["nishant"] #to delete some items
print(d2)

print(d2.copy())  #to make a copy of the dictionary

print(d2.get("prince"))  #to get value from dict

d2.update({"tom":"jerry"})  #to update some new data in dictionary
print(d2)

print(d2.keys())  #to print keys of dictionary

print(d2.items()) #to print items of dictionary



