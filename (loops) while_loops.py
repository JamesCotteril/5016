# While loop practice
#
# J T Cotterill
# October 2022

#Count up to a number

#Set start and end values
number = int(input("Please input a number...\n"))
target = 1

#Print every number between 1 and 6
while target <= number:
    print([target])
    target = target + 1

    if target > number:
        print("Completed")
        break
