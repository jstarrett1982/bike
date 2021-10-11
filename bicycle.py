# Assignment:  Creation of a Bicycle Class
# Jackie Starrett
# Purpose:  To create a class to describe bicycle attributes such as number of gears and wheels,
# brake type, and current gear in use.  The class also provides methods for the bike to do, such as reset to gear one, and increase/decrease gears.
# I was unable to create successfully create code for the increase and decrease gear functions, but I commented out the code for my attempts.
# The bicycle objects will be created in the main.py file.  The functions associated with the bike class are contained
# in this file, bicycle.py. These functions are called when the object is created in the main.py file.

# Creation of Bike class and a list of all its private properties and default values for each.
class Bike:
    __gears: int = 1
    __numberOfWheels: int = 2
    __currentGear: int = 1
    __brakeType: str = ""
    #__gearIncrement: int = 1  (I was unable to successfully incorporate this into my code.  This would have always been kept at the value of 1.

    # this line instantiates the class. Names of class attributes and default values follow the list.
    def __init__(self, gears=1, numberOfWheels=2, currentGear=1, brakeType="hand brakes"):

        # This sets all of the attributes within the class with the use of "self".  The last line for gearIncrement
        # is something that I tried to use for the increase/decrease gear function, which was unsuccessful.
        self.setGears(gears)
        self.setNumberOfWheels(numberOfWheels)
        self.setBrakeType(brakeType)
        self.setCurrentGear(currentGear)
        # self.setGearIncrement(gearIncrement)

    # This function returns the value for total number of gears on the bike
    def getGears(self) -> int:
        return self.__gears

    # This function allows the user to set the total number of available gears on the bikes, from one to 15.  If the class value is greater than one and less than 15, the function will pass.
    def setGears(self, gears: int) -> None:

        # This starts the exception-handling portion. All the functions in this file have this functionality.
        try:
            if 15 >= gears >= 1:
                self.__gears = gears
            else:
                print("invalid number of gears")
        except Exception as e:
            print(e)

    # This returns the number of wheels on the bike, which ranges from one to four.
    def getNumberOfWheels(self) -> int:
        return self.__numberOfWheels

    # This allows the user to set number of wheels on the bike (1 to 4). If a number is selected outside the range,
    # a warning message prints.
    def setNumberOfWheels(self, numberOfWheels: int):
        try:
            if 4 >= numberOfWheels >= 1:
                self.__numberOfWheels = numberOfWheels
            else:
                print("invalid number of wheels")
        except Exception as e:
            print(e)

    # This returns the value for brake type, which must be entered as either "hand brakes" or "foot brakes". Anything values other
    # than this that are put into the set function will cause an error message to be printed.

    def getBrakeType(self) -> str:
        return self.__brakeType

    # As with the other set functions, for the code to work currently, the attributes must be set before the values can be obtained through the
    # get function.  Here, brakeType is set either "hand brakes" or "foot brakes",based on what value is entered during object creation.

    def setBrakeType(self, brakeType: str):
        try:
            if brakeType == "hand brakes":
                self.__brakeType = brakeType
            elif brakeType == "foot brakes":
                self.__brakeType = brakeType
            else:
                print("invalid brake type")
        except Exception as e:
            print(e)

    # This function returns the current value associated with the bike gear.
    def getCurrentGear(self) -> int:
        return self.__currentGear

    # This function allows the user to change the bike gear in use to the number specified in the function call.
    # If the user tries to set the gear number higher than the total number of bike gears (self.__gears),then an error message will print
    def setCurrentGear(self, currentGear: int):
        try:
            if 1 <= currentGear <= self.__gears:
                self.__currentGear = currentGear
            else:
                print("that current gear value exceeds number of available gears on bike or is less than 1")
        except Exception as e:
            print(e)

    # The commented-out lines of code below represent one of the methods I tried to use to tackle the issue of increasing and decreasing the current gear value.
    # The gearIncrement get and set functions are listed below. The value put into these functions was to be used in the increase and decrease gear functions.

    # def getGearIncrement(self) -> int:
        # return self.__gearIncrement

    # def setGearIncrement(self, gearIncrement: int):
        # try:
            # if gearIncrement:
                # self.__gearIncrement = gearIncrement
        # except Exception as e:
            # print(e)

    # This function resets the current gear to the default value of 1.
    def resetGears(self, currentGear=1):
        try:
            if currentGear:
                self.__currentGear = currentGear
        except Exception as e:
            print(e)

    #The commented-out lines below represent more failed attempts at creating functions to increase or decrease the gear value by one.


    # def decreaseGear(self, gearIncrement=1):
    # try:
        # if self.__currentGear > int(gearIncrement):
            # self.__currentGear = self.__currentGear - gearIncrement (I also tried just using "1" and got rid of the gearIncrement attribute, neither way worked)
        # else:
            # print("you have reached the minimum gear, cannot decrease")
    # except Exception as e:
        # print(e)

    # def increaseGear(self, currentGear: int):
        # try:
            # if int(self.__currentGear) < 15:
                # self.__currentGear = self.__currentGear + 1 (I also tried using "gearIncrement" here, instead of 1)
            # else:
                # print("you have reached the highest gear")
        # except Exception as e:
            # print(e)
