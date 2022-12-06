# functions_practice.py
#
# @ author: J T Cotterill
# date: November 2022

#I chose three tasks, keeping them in one place I commented them out to work on the others. The code works and is tested.

#Task 1 - Complete
 
#def show_hello():
#    print("Hello and welcome!\n\n")

#def add_numbers(a, b):
#    print(a + b)

#show_hello()

#add_numbers(2, 3)

#Task 2 - Complete

#def show_message(x, y):
#    print(x * y)

#show_message(5, "Code!\n")

#Task 3 - Complete

import random

#randint required a range. This makes sense as a truly random int could be anywhere from 1 to infinity.
def display_random():
    x = random.randint(1, 100000000000)
    print(x)

#This while loop keeps a menu present. This function was useful for the menu in the development assignment.
while True:
    press_key = input("")
    if press_key == "r":
        display_random()
        continue
    else:
        break
