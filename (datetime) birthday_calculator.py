# birthday_calculator
#
# Author: J. T. Cotterill
# October 2022

from datetime import datetime
from datetime import timedelta

#Examples of some simple date calculations for future referral
print("125 days ago it was", datetime.today() - timedelta(days=125), ".\n")
print("In 2 weeks it will be", datetime.today() + timedelta(weeks=2), ".\n")

#Input 2 birthdays
birthday_input1 = input("Please enter the first birthday in the format DD Mmm YYYY: \n")
birthday_input2 = input("Please enter the second birthday in the format DD Mmm YYYY: \n")

#Cast to strptime for calculation
birthday_object1 = datetime.strptime(birthday_input1, '%d %b %Y')
birthday_object2 = datetime.strptime(birthday_input2, '%d %b %Y')

#Not sure if there's an easier method to minus the smallest or lowest object from the largest or highest, but I found this method using max and min
#Find oldest and youngest
oldest = min(birthday_object1, birthday_object2)
youngest = max(birthday_object1, birthday_object2)

#Print the calculation
print("The difference in age is approximately", youngest.year - oldest.year, "years")
