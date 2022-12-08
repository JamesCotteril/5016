# dictionary_datatypes.py
#
# From programiz.com
# December 2022

#Dictionary datatypes and functions

capital_city = {"Nepal": "Kathmandu", "England": "London"}
print("Initial Dictionary: ",capital_city)
#add an item to the dictionary
capital_city["Japan"] = "Tokyo"

print("Updated Dictionary: ",capital_city)

########

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}
print("Initial Dictionary: ", student_id)
#change an item in a dictionary
student_id[112] = "Stan"

print("Updated Dictionary: ", student_id)

########

student_id = {111: "Eric", 112: "Kyle", 113: "Butters"}

print("Initial Dictionary: ", student_id)
#delete an item from the dictionary
del student_id[111]

print("Updated Dictionary ", student_id)
