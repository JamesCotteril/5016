# shape_area_calculator.py
#
# J T Cotterill
# October 2022

#Welcome and instructions
option_selected = 'nil'

while True:
    print("Welcome to the shape calculator. Please select and input from the following:")
    option_selected = input(str("\nArea - Calculate the area.\nVolume - Calculate the volume.\nExit - Exit the program.\n")).lower()
                          
#area
    if option_selected == 'area':
              while True:
                  x = int(input("Please enter an x value below 10.\n"))
                  if x > 10:
                      print("Error. Number is too large.")
                  if x < 10:
                                    break                
              while True:
                  y = int(input("Please enter a y value below 8.\n"))
                  if y > 8:
                      print("Error. Number is too large.")
                  if y < 8:
                                    break                  
                            
              area_calculation = (10 * 3 * 2) + (8 * 10 - x * y)
              print("Area is", area_calculation)
              option_selected = 'nil'
#volume
    if option_selected == 'volume':
            while True:
                  x = int(input("Please enter an x value below 10.\n"))
                  if x > 10:
                      print("Error. Number is too large.")
                  if x < 10:
                                    break
            while True:
                  y = int(input("Please enter a y value below 8.\n"))
                  if y > 8:
                      print("Error. Number is too large.")
                  if y < 8:
                                    break

            volume_calculation = (10 * 3 * 8) - (x * y * 3)
            print("Volume is", volume_calculation)
            option_selected = 'nil'

#exit
    if option_selected == 'exit':
              break






