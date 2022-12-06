# (functions) functions_practice2.py
#
# @ author: J T Cotterill
# date: November 2022

#I chose 3 tasks and completed them here.

#Challenge 1 - Complete - Get user input and run through a pre-defined method to display the input

#def display_details(param_name, param_number):
#    print("Hello there, my name is {0} and my phone number is {1}.\n".format(param_name, param_number))

#while True:
#    name_input = input("Please input your name:\n")
#    print("\nThank you\n")
#    number_input = input("Please input your phone number:\n")
#    print("\nThank you\n")
#    display_details(name_input, number_input)

#Challenge 4 - Complete - Make a function to print the sum of a list

#stored_list = [21, 32, 43, 22, 1, 5, 18]

#def total_list():
#    print(sum(stored_list))

#total_list()

#Challenge 6 - Complete - Print even numbers in a list and odd numbers in a list

stored_list = [21, 32, 43, 22, 1, 5, 18]

def only_even_numbers(param_list):
#By using sorted on the list first, the numbers displayed are printed in ascending order
    sorted_param_list = sorted(param_list)
    for i in sorted_param_list:
#The % operator finds the remainder when a number is divided. If a remainder is 0 when divided by 2 then it is an even number
        if i % 2 == 0:
            print(i)
            
def only_odd_numbers(param_list):
    sorted_param_list = sorted(param_list)
    for i in sorted_param_list:
        if i % 2 != 0:
            print(i)
            
print("Test case assertion: displays 18, 22, 32")
only_even_numbers(stored_list)

print("Test case assertion: displays 1, 5, 21, 43")
only_odd_numbers(stored_list)
