#more_functions.py
#
# J T Cotterill
# November 2022

#Practice from the more functions tab. The code has been tested.

#Challenge 2 - Complete - Cut and print the first and last numbers in a list

#list_1 = [5, 10, 15, 20, 25]

#def first_and_last(param_list):
#Use pop to remove  one item from a list
#    first = param_list.pop(0)
#Using negative index to pop the last item, regardless of the length of the list
#    last = param_list.pop(-1)
#Add to list
#    new_list = [first, last]
#    return new_list


#print(first_and_last(list_1))

#Challenge 6 - complete - Finish the rhyme


#count = 99

#Include the return function in the method to update the counter
#def one_bottle_down(count_param):
#    print(count_param, "bottles of beer on the wall,", count_param, "bottles of beer.\nTake one down, pass it around,", (count_param - 1), "bottles of beer on the wall.")
#    return (count_param - 1)

#while count >= 1:
#    count = one_bottle_down(count)

#Challenge 5 - complete - Count the length of words in a list

list_1 = ["apple", "four", "porcupine", "walrus"]
#create a new list for lengths
list_1_lengths = []

def get_lengths(list_1):
    for i in range(0, len(list_1)):
        #Grab length of all items in the list with number variable
        number = len(list_1[i])
        #Add all numbers to the length list
        list_1_lengths.append(number)

get_lengths(list_1)
print(list_1_lengths)
    
    
    
