#better_countdown.py
#
# from programiz.com
# December 2022

#This is more research into more advanced code and showed me a cleaner way to produce a countdown timer.
import time

def countdown(time_sec):
    while time_sec:
      #This divmod function seems to provide two numbers in a tuple. One being the result of dividing the former by the latter and the other being the remainder thereof.
        mins, secs = divmod(time_sec, 60)
        #For a countdown timer, this format lokks very clear and clean.
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        #/r is a carriage return. This will move the cursor back to the front of the console and overwrite anything already there.
        #NOTE: This doesn't work properly in some compilers, but when run with the console from python.org, will work as intended.
        print(timeformat, end='\r')
        #This function, time.sleep will pause the time for a second. Without htis line of code, the results will all be displayed instantly.
        time.sleep(1)
        #Reduce seconds by one.
        time_sec -= 1

    print("stop")

countdown(5)

#If I need to implement a countdown timer in future, this is the format I would like to use. It displays in minutes and seconds and it also overwrites itself, 
#which keeps the console clear.
