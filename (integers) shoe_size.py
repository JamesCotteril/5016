# shoe_size.py (Rounded Numbers)
#
# @ author: J. T. Cotterill
# date: October 2022
 
# variable set to float
my_size = float(input("Enter your shoe size:\n"))
print("The type of my_size is ", type(my_size),"\n")
print("my_size is ", my_size,"\n")
 
print("Casting to an integer...\n")
# variable cast to integer

#Code to round a float to the nearest integer, then cast
my_size = round(my_size, 0)
my_size = int(my_size)
 
print("The type of my_size is now ", type(my_size),"\n")
print("my_size is ", my_size,"\n")

#I added a round line of code to round a number to cast to an integer. Just experimenting with floats/integers.
