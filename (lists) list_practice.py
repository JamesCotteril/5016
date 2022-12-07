# list_practice.py
#
# author J T Cotterill
# date: November 2022

#Completed 3 tasks and commented out a couple. The code has been tested.

list_1 = [23, 66, 23, 12]
list_2 = [1, 19, 4, 8]
list_3 = ["land of ", "the ", "the long white cloud"]

#Challenge 1 - Complete - Sum and average of lists of numbers
import statistics
choice = 0
print("The 2 lists are", list_1, "and", list_2,"\n")

while choice == 0:
    choice = int(input("Please enter 1 to see the sum of the two lists, 2 to see the average of the two lists, or 0 to quit:\n"))
    if choice == 1:
        print("The sum of the two lists is", sum(list_1 + list_2),"\n")
        choice = 0
        continue
    if choice == 2:
        print("The average of the two lists is", statistics.mean(list_1 + list_2),"\n")
        choice = 0
        continue
    if choice == 0:
        break
    else:
        print("\n***\nPlease select a valid option (1 or 2).\n***\n")
        choice = 0
        continue

#Challenge 9 - Complete - Sort and print a list by length

#sorted_list_3 = sorted(list_3, key = len)
#final_display = "".join(sorted_list_3)
#print(final_display)

#Challenge 5 - Complete - Find odd numbers in a list and print them

#for i in list_1:
#    if i % 2 != 0:
#        print(i)

#Challenge 8 - Complete - Choose random items from both lists. If they are the same, chose again

#import random

#item_1 = (random.choice(list_2))
#item_2 = (random.choice(list_2))

#while item_1 == item_2:
#    item_2 = (random.choice(list_2))

#print(item_1, "and", item_2)
