# Auckland Grammar School
#
# @ author: J. T. Cotterill
# date: October 2022

distance = float(input('Enter distance from school(km):\n'))
age = int(input('Enter age of student:\n'))
right = str(input('Does the student have the right to stay in New Zealand? (yes or no):\n')).lower()
international_student = str(input('Will the student be paying international fees? (yes or no):\n')).lower()

#Validate distance from school

if distance <= 4.0:
    valid_distance = True

else:
    valid_distance = False

#Validate age

if age <= 18:
    valid_age = True

else:
    valid_age = False

#Validate right

if right == 'yes':
    valid_right = True

else:
    valid_right = False

#Check for international fees

if international_student == 'yes':
    valid_international_student = True

else:
    valid_international_student = False

#Check if domestic student is eligible or if international student is eligible

if valid_distance and valid_age and valid_right == True:
    print('The student is an eligible domestic student.')

elif valid_international_student and valid_age == True:
    print('The student is an eligible international student.')

else:
    print('The student is ineligible to enroll.')
