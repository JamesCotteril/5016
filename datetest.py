# Make a Birthday Calculator
#
# Author: J. T. Cotterill
# October 2022

from datetime import datetime
from datetime import timedelta


print("125 days ago it was", datetime.today() - timedelta(days=125), ".\n")
print("In 2 weeks it will be", datetime.today() + timedelta(weeks=1), ".\n")

birthday_input1 = input("Please enter the first birthday in the format DD Mmm YYYY: \n")
birthday_input2 = input("Please enter the second birthday in the format DD Mmm YYYY: \n")

birthday_object1 = datetime.strptime(birthday_input1, '%d %b %Y')
birthday_object2 = datetime.strptime(birthday_input2, '%d %b %Y')

oldest = min(birthday_object1, birthday_object2)
youngest = max(birthday_object1, birthday_object2)

print("The difference in age is approximately", youngest.year - oldest.year, "years")
