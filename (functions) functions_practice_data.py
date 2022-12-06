# functions_practice_data.py
#
# J T Cotterill
# November 2022

#I chose 3 tasks and completed them here. The code has been tested.

#Challenge 3 - Complete - A program which calculates the cost of parking

#cost = 0

#print("Parking Cost Calculator\n")
#print("This program calculates the cost of parking.\n$4 for the first two hours and $3 every hour thereafter.") 

#def get_cost(param_hours):
#    param_cost = (hours-2) * 3 + 4
#    return param_cost

#hours = int(input("Enter the number of parking hours:\n"))

#print("The cost of parking for {0} hours is ${1}.".format(hours, get_cost(hours)))

#Challenge 5 - Complete - A countdown timer

#from datetime import datetime, timedelta

#The period of time for each count
#period = timedelta(seconds = 1)

#Counts using a period of time 
#next_time = datetime.now() + period

#def tick_down(param_selection, next_time, period):
#The while loop keeps the code running, and if a second passes then the selected time is reduced by one. Rinse and repeat.
#    while  param_selection > 0:
#        if next_time <= datetime.now():
#            print("", param_selection)
#            param_selection -= 1
        
#            next_time += period
    

#print("Welcome to the countdown timer.\n")
#selection = int(input("Please enter the number of seconds to count down...\n"))
#print("Starting up...\n")

#tick_down(selection, next_time, period)    
#print("Time's up!!")

#Challenge 12 - Complete - An online store price calculation

#Only one line of code turns an input quantity to a price
print("Welcome to the online store, please enter the quantity of each item you wish to purchase:\n")
greenstone_koru = 265 * int(input("Greenstone Koru carving, quantity needed?\n"))
rimu_tiki = 42 * int(input("Greenstone Koru carving, quantity needed?\n"))
manaia_bone = 311 * int(input("Greenstone Koru carving, quantity needed?\n"))

#Run calculations in order. Could be done more efficiently in one line of code instead
def get_price(koru, tiki, bone):
    total = koru + tiki + bone
    gst = 0.15 * total
    grand_total = total + gst
    print("Thank you!\nSubtotal is: {0}\nGST @ 15% is: {1}\nGrand Total is: {2}".format(total, gst, grand_total))

#plug in parameters
get_price(greenstone_koru, rimu_tiki, manaia_bone)
