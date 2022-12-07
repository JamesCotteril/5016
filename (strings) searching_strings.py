# searching_strings.py
#
#  J T Cotterill
# November 2022
#Searching strings will play a big role in the assignment. I collated answers for the questions here. I tested all of them in python.

#Challenge 1 - Complete - Count a character in a string

#stored_string ="The first rule of fight club is: do not talk about fight club."
#counter = 0
#print("The string is:", stored_string)

#print("The number of blank spaces is {0}\n".format(stored_string.count(" ")))

#Challenge 3 - Complete - Display if a string starts with a certain phrase

#input_string = str(input("Please input some text:\n").title())
#print("Does this string start with '"+input_string+"'?: {0}\n".format(stored_string.startswith(input_string)))

#Challenge 5 - Complete - Find the index number of a character or characters in a string

#fight_index = stored_string.find("fight")
#second_fight_index = stored_string.find("fight", 29)
#print("The index position of the first instance of 'fight' is {0}".format(fight_index))
#print("The index position of second instance of 'fight' is {0}".format(second_fight_index))

#Challenge 9 - Complete - Search for at least one capital letter and one number in a password, and validate it.

import re
password_confirmed = False
while password_confirmed == False:
    
    password_input = input("Please enter password with at least one number and one capital letter:\n")
    numbers = re.findall('[0-9]+', password_input)
    capitals = re.findall('[A-Z]', password_input)
    if capitals != [] and numbers != []:
        password_confirmed = True
        print("Password confirmed.")
        break
    else:
        print("Error. Please include a number and a capital letter.")
       continue

#Challenge 7 - Complete - make a username using an email address by searching for index numbers

#email_input = input("Please enter your email address:\n")
#period_index = email_input.find(".")
#at_index = email_input.find("@")

#username = '{0}{1}'.format(email_input[0], email_input[period_index+1:at_index])
#print(username)
