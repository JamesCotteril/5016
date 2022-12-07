# while_loops3.py
#
# J T Cotterill
# October 2022

#Login attempts

#Set password and number of tries
password = str('secret')
number_of_tries = 3

while True:
    attempt = str(input("Please enter your password to proceed...\n"))
#Breaks the loop if the last try is used
    if number_of_tries == 1:
        print('Error. Number of tries exceeded. Terminating...')
        break
#Password is correct    
    if attempt == 'secret':
        print('Password confirmed. Logging in...')
        break
#Exit if exit is input
    if attempt == 'exit':
        print('Exit confirmed. Terminating...')
        break
#Decrease number of tries if the password is wrong
    else:
        number_of_tries = number_of_tries - 1
        print("Sorry that's incorrect. You have", number_of_tries, "tries remaining. Please try again.\n")
        
        
    
    
    
