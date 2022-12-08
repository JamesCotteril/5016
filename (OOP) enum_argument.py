# enum_argument.py
#
# example from programiz.com
# December 2022

#In an effort to expand my knowledge of OOP, I found an example of another method of making a class using something called enum.

from enum import Enum

class Day(Enum):
    MONDAY = 1.5
    TUESDAY = 2
    WEDNESDAY = 3

# print the enum member
print(Day.MONDAY)

# get the name of the enum member
print(Day.MONDAY.name)

# get the value of the enum member
print(Day.MONDAY.value)

#From this example, there are only two attributes assigned to objects in the day class. One is a name, the other is a value.
#I attemped to change the value to another symbol to see how this affected the result.

class Month(Enum):
    January = J
    February = F
    March = M

# print the enum member
print(Day.January)

# get the name of the enum member
print(Day.January.name)

# get the value of the enum member
print(Day.January.value)

#This resulted in 
#Traceback (most recent call last):
#  File "C:/Users/GGPC/Desktop/Done/enum.py", line 27, in <module>
#    class Month(Enum):
#  File "C:/Users/GGPC/Desktop/Done/enum.py", line 28, in Month
#    January = J
#NameError: name 'J' is not defined
#
#So I can conclude this enum module will only work with a name and a value with an assigned integer (not a string), 
#after further testing I discovered this number can also be a float.
