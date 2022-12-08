words = ["Amazing", "Green", "Python", "Code"]

with open("famous_quotes.txt", "w") as file:
    for word in words:
        file.write(word + "\n")

with open("famous_quotes.txt", "r") as file:
    for line in file:
        print(line)

print('-----------------------------')


with open("famous_quotes.txt", "r") as file:
   print("Print only the first line:\n{0}".format(file.readline()))


print('-----------------------------')

with open("famous_quotes.txt", "r") as file:
    all_lines_variable = file.readlines()
    print("Test assertion: Print only Python:\n{0}".format(all_lines_variable[2]))

import os

if os.path.exists("famous_quotes.txt"):
  os.remove("famous_quotes.txt")
  print("famous_quotes.txt deleted")
else:
  print("This file doesn't exist")
