class employee:  # create a class
    var = 8
    no_of_leaves = 8

    """USING CONSTRUCTORS"""

    def __init__(self, aname, asalary, arole):  # __init__ is a constructor
        self.name = aname  # take the name in  variable aname.
        self.salary = asalary  # take the salary in  variable asalary.
        self.role = arole  # take the role in  variable arole

    """ using SELF arguments."""

    def printdetails(self):  # define a function with self argument or we can take any variable argument

        return f"Name : {self.name},And salary : {self.salary},And role : {self.role}."  # self is here the
        # function on which we want to worked

    """USING DECORATORS: to change class instances"""

    @classmethod  # using decorators
    def change_leaves(cls, new_leaves):  # cls acess class and new_leaves is the argument we can change it as we want.
        cls.no_of_leaves = new_leaves

    """tutorial 57: using alternative constructors """

    @classmethod  # creting class using alternative decorator and constructors
    def from_str(cls, string):  # def class
        param = string.split("-")  # convert to list
        print(param)
        return cls(param[0], param[1], param[2])  # using index separated list
        return cls(*string.split("-"))  # using one liner

    """Tut 58 using static method"""

    @staticmethod  # created as a decorator as a class method
    def printgood(string):  # define good print
        print("this is a very good:" + string)  # print by adding the string
        return  # it return NONE


class player:  # making another class
    var = 9
    no_of_games = 4

    def __init__(self, name, game):
        self.name = name
        self.game = game

    def printdetails(self):
        return f"Name :{self.name} game:{self.game}"

class coolprogrammmer(employee, player):  # multiple inheritance
    var = 10
    language = "c++"
    def printlanguage(self):
        print(self.language)

prince = coolprogrammmer("prince", 899, "cricket")
prinwce = player("ram", "hock")
prisnce = employee("prince", 899, "cricket")
print(prisnce.printdetails())
print(prince.printdetails())
print(prinwce.printdetails())
prince.printlanguage()
print(prince.var)  # it print the var of the class which is first.