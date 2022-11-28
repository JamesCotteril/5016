# OOP.py
#
# J T Cotterill
# November 2022

class Person:
    def __init__(self, age, address, gender, height):

        self.age = age
        self.address = address
        self.gender = gender
        self.height = height

    def __str__(self):
        return f"Hello my gender is {self.gender}, my age is {self.age}, my address is {self.address} and my height is {self.height}"



harry = Person(36, "24 Opawa Road", "male", 1.92)

sarrah = Person(34, "32 Te Whariki Street", "female", 1.45)

print(harry.__str__())

print(sarrah.__str__())


