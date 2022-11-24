# functions_practice_data.py
#
# J T Cotterill
# November 2022


#Challenge 3 - Complete

#cost = 0

#print("Parking Cost Calculator\n")
#print("This program calculates the cost of parking.\n$4 for the first two hours and $3 every hour thereafter.") 

#def get_cost(param_hours):
#    param_cost = (hours-2) * 3 + 4
#    return param_cost

#hours = int(input("Enter the number of parking hours:\n"))

#print("The cost of parking for {0} hours is ${1}.".format(hours, get_cost(hours)))

#Challenge 5 - Complete

#from datetime import datetime, timedelta

#period = timedelta(seconds = 1)

#next_time = datetime.now() + period

#def tick_down(param_selection, next_time, period):
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

#Challenge 12 - Complete

print("Welcome to the online store, please enter the quantity of each item you wish to purchase:\n")
greenstone_koru = 265 * int(input("Greenstone Koru carving, quantity needed?\n"))
rimu_tiki = 42 * int(input("Greenstone Koru carving, quantity needed?\n"))
manaia_bone = 311 * int(input("Greenstone Koru carving, quantity needed?\n"))

def get_price(koru, tiki, bone):
    total = koru + tiki + bone
    gst = 0.15 * total
    grand_total = total + gst
    print("Thank you!\nSubtotal is: {0}\nGST @ 15% is: {1}\nGrand Total is: {2}".format(total, gst, grand_total))

get_price(greenstone_koru, rimu_tiki, manaia_bone)
