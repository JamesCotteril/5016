# nzquiz.py
#
# @ author: J. T. Cotterill
# date: October 2022

import time
time_start = time.perf_counter()
correct = 0

#Question 1
print('Question 1:\nAotearoa means land of the...\n(a) Maori (b) People (c) Long White Cloud')
one_correct = 'c'
one_answer = input(str('Enter your answer:\n')).lower()

if one_answer == one_correct:
    print('Well done! You recieve one point!')
    correct = correct + 1
else:
    print("Sorry! That's not right. Try the next one!")


#Question 2
print('Question 2:\nFemale voting was approved in NZ in...\n(a) 1893 (b) 1912 (c) 1867')
two_correct = 'a'
two_answer = input(str('Enter your answer:\n')).lower()

if two_answer == two_correct:
    print('Well done! You recieve one point!')
    correct = correct + 1
else:
    print("Sorry! That's not right. Try the next one!")
    
#Question 3
print('Question 3:\nWhat percent of NZ is classified as a national reserve?\n(a) 23% (b) 30% (c) 36%')
three_correct = 'b'
three_answer = input(str('Enter your answer:\n')).lower()

if three_answer == three_correct:
    print('Well done! You recieve one point!')
    correct = correct + 1
else:
    print("Sorry! That's not right. Try the next one!")
    
#Question 4
print('Question 4:\nFor every person living in New Zealand, how many sheep are there?\n(a) 10 (b) 5 (c) 8')
four_correct = 'a'
four_answer = input(str('Enter your answer:\n')).lower()

if four_answer == four_correct:
    print('Well done! You recieve one point!')
    correct = correct + 1
else:
    print("Sorry! That's not right. Try the next one!")
    
#Question 5
print('Question 5:\nRoughly how many years ago did the Maori first arrive in New Zealand?\n(a) 700 (b) 800 (c) 600')
five_correct = 'b'
five_answer = input(str('Enter your answer:\n')).lower()

if five_answer == five_correct:
    print("Well done! You recieve one point! Let's tally up your score\n")
    correct = correct + 1
else:
    print("Sorry! That's not right. Hope you did better on the other questions. Let's tally up your score.\n")

#Tally up and display timer

print("Your total score was", correct, "out of 5.")
if correct <= 2:
    print('You should do more study!')
elif correct <=4 and correct >=3:
    print('Nicely done!')
else:
    print("Perfect score! You're so clever!")

time_end = time.perf_counter()
time_taken = round(time_end - time_start)

print("You took", time_taken, "seconds.")
