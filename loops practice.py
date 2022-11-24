# loopspractice.py
#
# @ author: J T Cotterill
# date: November 2022
 

# Question 1 - Complete
#for i in range(1500, 2700):
#        if (i % 7 == 0) and (i % 5 == 0):
#            print(i)

#Question 3 - Complete
#import random
#number = random.randint(1, 9)

#while True:
#    guess = int(input("I'm thinking of a number between 1 and 9, have a guess!\n"))

#    if guess == number:
#            print("Well guessed!")
#            break

# Question 8 - Complete

#for i in range(0, 6):
#    if i == 3 or i == 6:
#        continue
#    print(i)


#Question 10 - Complete
#for i in range(1, 51):
#    if (i % 3 == 0) and (i % 5 == 0):
#        print("FizzBuzz")
#        continue
        
#    if (i % 3 == 0) and (i % 5 != 0):
#        print("Fizz")
#        continue
        
#    if (i % 3 != 0) and (i % 5 == 0):
#        print("Buzz")
#        continue
        
#    else:
#        print(i)

#Question 31 - Complete
#age_in_human_years = int(input("Please enter the dog's age in human years...\n"))
#age_in_dog_years = 0

#for i in range(1, age_in_human_years + 1):
#    if i <= 2:
#        age_in_dog_years = age_in_dog_years + 10.5
#        continue

#    if i >= 3:
#        age_in_dog_years = age_in_dog_years + 4
#        continue

#print("The dog's age in dog years is", age_in_dog_years)

#Question 36 - Complete

#while True:
                    
#    side_a = float(input("Please input the first side of your triangle, decimal figures are acceptable...\n"))
#    side_b = float(input("Please input the second side of your triangle, decimal figures are acceptable...\n"))
#    side_c = float(input("Please input the third side of your triangle, decimal figures are acceptable...\n"))
#    side_list = [side_a, side_b, side_c]
#    two_lowest = [i for i in side_list if i != max(side_list)]
#    longest = max(side_list)

#    if side_b == side_c == side_a:
#        print("This shape is an equilateral triangle.")
#        continue

#    elif side_a != side_b != side_c:
#        if longest < sum(two_lowest):
#            print("These measurements are incompatible. Please check again.")
#            continue
#        print("This shape is a scalene triangle.")
#        continue
    
#    else:
#        if longest < sum(two_lowest):
#            print("These measurements are incompatible. Please check again.")
#            continue
#        print("This shape is an isosceles triangle.")
#        continue


#Question 42 - Complete

#print("Input some integers to calculate their sum and average. Input 0 to exit.")

#count = 0
#sum = 0.0
#number = 1
#average = 0.0

#while number != 0:
#    number = int(input(""))
#    count += 1
#    sum = sum + number
#    average = sum / count
#    print("Average and sum of the numbers entered are", average, "and", sum)

#Question 43 - Complete

#number =  int(input("Input a number: "))

#for i in range (1, 11):
#    print(number, "x", i, "=", (number * i),"\n")

#Question 21 - Complete ( Question 27 also complete )

#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if (row == 0 or (column == 3 and column != 0 and column < 7)):  
#            result_str=result_str+"*"    
#        else:      
#            result_str=result_str+" "
            
#Test Assertion: Should display a T instead of an L. Success.
#    result_str=result_str+"\n"    
#print(result_str);

#Question 22 - Complete
#result_str="";    
#for row in range(0,7):    
#    for column in range(0,7):     
#        if (column == 1 or column == 5 or (row == 5 and (column == 2 or column == 4)) or (row == 4 and column == 3)):  
#            result_str=result_str+"* "    
#        else:      
#            result_str=result_str+"  "    
#    result_str=result_str+"\n"
#Test Assertion: Should display a W instead of an M. Success.    
#print(result_str);

#Question 30 - Complete
#result_str = "";
#for row in range(0, 7):
#    for column in range(0, 7):
#        if row == 0 or row == 6 or (row == 1 and column == 5) or (row == 2 and column == 4) or (row == 3 and column == 3) or (row == 4 and column == 2) or (row == 5 and column == 1):
#            result_str = result_str + "* "
#        else:
#            result_str = result_str + "  "
#    result_str = result_str + "\n"
#print(result_str);
