# shapes.py
#
# @ author: A. N. Other
# date: September 2016
# Using * to draw shapes 
user_input = int(input("Please enter a number for the size"
                       "of the shape you wish to create."))
 
for i in range(user_input):
    for j in range(i):
        print('* ', end="")
    print('')
 
for i in range(user_input, 0, -1):
    for j in range(i):
        print('* ', end="")
    print('')
