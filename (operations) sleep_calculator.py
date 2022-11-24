# sleep_calculator.py
#
# author: A. N. Other
# date: October 2022

print ("Welcome. I'm your Sleep Calculator.\n")
user_name = input("Please enter your name...\n")
user_yob = int(input("Please enter your year of birth...\n"))
 
print("Thank you for your input\n")
print(user_name.capitalize()+ ", you have slept for", (2022 - user_yob)*365*7, "hours.")
