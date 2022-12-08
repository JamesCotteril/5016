# read_and_write_files.py
#
# freecodecamp.org and my own additions
# December 2022


words = ["Amazing", "Green", "Python", "Code"]

#These write and read functions also work without using the extra letter variable, as this is the default use
with open("famous_quotes.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

with open("famous_quotes.txt", "r") as file:
    for line in file:
        print(line)

print('-----------------------------')

#The commands readline() and readlines() will read the first line of a text file and all lines repsectively
with open("famous_quotes.txt", "r") as file:
   print("Print only the first line:\n{0}".format(file.readline()))


print('-----------------------------')

#Using a variable containing all lines of a file we can search and read specific lines from a text file
with open("famous_quotes.txt", "r") as file:
    all_lines_variable = file.readlines()
    #Note: For the format of this line, you need to use a number which is your target line minus one
    print("Test assertion: Print only Python:\n{0}".format(all_lines_variable[2]))

import os
#Use these to delete files in the same directory as the python file.
if os.path.exists("famous_quotes.txt"):
  os.remove("famous_quotes.txt")
  print("famous_quotes.txt deleted")
else:
  print("This file doesn't exist")

#Without the ability to write, store, read and delete files a program is severely limited in what it can do. With these codes I could produce an upgraded
#version of the ticketing system assignment that stores tickets as text files, and interact with them, rewriting them when responded to, moving them to an archive
#folder when closed, etc.
