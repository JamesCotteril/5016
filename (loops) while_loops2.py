# while_loops2.py
#
# J T Cotterill
# October 2022

#Sum of all numbers between 1 and a chosen number

number_input = int(input("Please input a number...\n"))
target = 0

while number_input >= 1:
    target += number_input
    number_input = number_input - 1

    if number_input == 0:
        print("Sum is", target)
        break
    
