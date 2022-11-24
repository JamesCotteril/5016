# While loop practice
#
# J T Cotterill
# October 2022

password = str('secret')
number_of_tries = 3

while True:
    attempt = str(input("Please enter your password to proceed...\n"))

    if number_of_tries == 1:
        print('Error. Number of tries exceeded. Terminating...')
        break
    
    if attempt == 'secret':
        print('Password confirmed. Logging in...')
        break

    if attempt == 'exit':
        print('Exit confirmed. Terminating...')
        break

    else:
        number_of_tries = number_of_tries - 1
        print("Sorry that's incorrect. You have", number_of_tries, "tries remaining. Please try again.\n")
        
        
    
    
    
