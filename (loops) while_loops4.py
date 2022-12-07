# while_loops4.py
#
# J T Cotterill
# October 2022
# Guess a secret number given clues to increase or decrease the guess

secret_number = 56
number_of_tries = 0
previous_attempt = -1

print("I'm thinking of a number between 1 and 100... Have a guess!\n")

while True:
    attempt = int(input("Go on. Guess!\n"))
#If user inputs the same guess twice, don't count it    
    if attempt == previous_attempt:
        print("You just guessed that one! Try something else!")
        #Set the previous attempt variable to check the next guess against it
        previous_attempt = attempt
    
    if attempt > secret_number and attempt != previous_attempt:
        print('Too high! Try again\n')
        number_of_tries = number_of_tries + 1
        previous_attempt = attempt
        
    if attempt < secret_number and attempt != previous_attempt:
        print('Too low! Try again\n')
        number_of_tries = number_of_tries + 1
        previous_attempt = attempt
        
    if attempt == secret_number:
        print("Congratulations! It was", secret_number)
        print("It took you", number_of_tries, "tries.")
        break
