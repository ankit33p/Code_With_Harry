class electronicdevice:  # create a super class
    electricity = 3



class pocket_gadget(electronicdevice):  # create a sub class
    running = 4
    def __init__(self, power, hour):
        self.power = power
        self.hour = hour
    def isrunning(self):

        return f"The power consume is {self.power} in running  {self.hour} hours."


class phone(pocket_gadget):  #create sub and super class child
    usage = 10
    def __init__(self, power, hour, usage):
        self.power = power
        self.hour = hour
        self.usage = usage
    def isusage(self):
        return f"The power consume is {self.power} in running{self.hour}hours and usage is {self.usage}"

iron = electronicdevice
speaker = pocket_gadget("watt", 6)
lava = phone("watt",10,"46 unit")

print(lava.isusage())
print("The power consumed is ",lava.electricity)  # inherits the features of super class
print(lava.isrunning())  # inherits the features of sub class


