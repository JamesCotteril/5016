# While loop practice 2
#
# J T Cotterill
# October 2022

number_input = int(input("Please input a number...\n"))
target = 0

while number_input >= 1:
    target += number_input
    number_input = number_input - 1

    if number_input == 0:
        print("Sum is", target)
        break
    
