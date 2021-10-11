# File:  Creation of bicycle objects
# by: Jackie Starrett
# Description:  The file imports our bike class then calls the functions within that class to create bike objects.

# This imports the "Bike" class from the "bicycle" python file. Now, we can use all the functions within the class by calling them below.
from bicycle import Bike

# This creates a bike object by calling the class.  No values are given, so default values are assigned to each attribute.
mountaineer = Bike()

# these print statements will show us the default values which have been assigned to the mountaineer Bike object.
print()
print(mountaineer.getNumberOfWheels())
print(mountaineer.getBrakeType())
print(mountaineer.getGears())
print(mountaineer.getCurrentGear())
print()

# This puts a pause in the program so user can see results in smaller sections. I will use this multiple times.
input("press [ENTER] to continue")
print()

# Now, I will change up the values for the attributes to something other than the default and print results
mountaineer.setGears(10)
mountaineer.setBrakeType("foot brakes")
mountaineer.setNumberOfWheels(3)
mountaineer.setCurrentGear(8)
print("mountaineer has ", (mountaineer.getNumberOfWheels()), "wheels and", (mountaineer.getGears()), "gears")
print("mountaineer has", (mountaineer.getBrakeType()), "and is at the", (mountaineer.getCurrentGear()), "gear")
print()
input("press [ENTER] to continue")
print()

#Now, I will reset the current gear back to the default value of one
mountaineer.resetGears()
print("mountaineer is now at the default gear of ", (mountaineer.getCurrentGear()))
print()
input("press [ENTER] to continue")
print()

#Now, I will show what happens when I try to give mountaineer electric brakes
mountaineer.setBrakeType("electric")
#This will display an error message about invalid brake types.
# In the print statement, it will get the brake type currently assigned to mountaineer, since it couldn't use "electric"
print("mountaineer has", (mountaineer.getBrakeType()))
print()
input("press [ENTER] to continue")
print()

#Now, I will show what happens when I put invalid numbers into my setNumberOfWheels and setCurrentGear functions
mountaineer.setNumberOfWheels(0)
mountaineer.setNumberOfWheels(5)
mountaineer.setCurrentGear(0)
mountaineer.setCurrentGear(11)
print("mountaineer has", (mountaineer.getNumberOfWheels()), "wheels and is at the", (mountaineer.getCurrentGear()), "gear")
#Since it couldn't assign the invalid values, it will get and print the most-recently assigned values for currentGear and number of wheels








