# Auckland Grammar School
#
# @ author: J. T. Cotterill
# date: November 2022



while True:
    distance = float(input('Enter distance from school(km):\n'))
    age = int(input('Enter age of student:\n'))
    right = str(input('Does the student have the right to stay in New Zealand? (yes or no):\n')).lower()
    international_student = str(input('Will the student be paying international fees? (yes or no):\n')).lower()
#Check if domestic student is eligible or if international student is eligible

    if (distance <= 4.0) and (age <= 18) and (right == 'yes') == True:
        print('The student is an eligible domestic student.')

    elif (international_student == 'yes') and (age <= 18) == True:
        print('The student is an eligible international student.')

    else:
        print('The student is ineligible to enroll.')
