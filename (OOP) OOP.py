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

#While I understand the general idea of classes and class methods. I'm still unsure of why it's important to seperate things into different classes
#I imagine this will become clearer as I work more with OOP languages like python but during the assignment we did, it didn't seem relevant as there
#were only 2 classes, and the main class was only made for the purpose of executing the program. With a more complex program with more than one
#class that contain more functions and different objects made with those classes, I would be able to see OOP in more depth.
