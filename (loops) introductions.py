# introductions.py
# Introduce yourself to your computer
#
# author: J. T. Cotterill
# October 2022

#Enter name and display
name = input(str("What's your name?\n"))
print('Your name is', name.capitalize() + ".")
#Check if correct
positive = input(str('Is that right?\n')).lower()


#Name is incorrect
while positive != 'yes':
  

    if positive == 'no':
        print('Then why would you say that?')
    
        name = input(str("What's your real name?\n"))
        print('Your name is', name.capitalize() + ".")

        positive = input(str('Is that right?\n')).lower()

#Seek clarification
    else:
        print("I don't understand.")
        positive = input(str("Please reply yes or no, is that your name?\n")).lower()
        
    

#Name is correct
if positive == 'yes':
    print('Nice to meet you', name.capitalize() + '!')


