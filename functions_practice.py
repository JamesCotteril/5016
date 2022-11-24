# functions_practice.py
#
# @ author: J T Cotterill
# date: November 2022

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

def display_random():
    x = random.randint(1, 100000000000)
    print(x)

while True:
    press_key = input("")
    if press_key == "r":
        display_random()
        continue
    else:
        break
