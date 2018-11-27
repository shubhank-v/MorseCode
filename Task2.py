#######################################Task2#############################################
#                           Name: Shubhank Vijayvergiya                                 #
#                           Student Id: 29421934                                        #
#                           Start Date: 22/03/2018                                      #
#                           Last Modified Date: 29/03/2018                              #
#######################################Task2#############################################
# import regular expression
import re
'''
Description:
Taking input from user and displaying it on console. Multiple inputs are separated by '*' symbol.
Hitting Enter key will terminate the program, valid input will be displayed on console.
'''
# Define list to store input
morse_code_list =[]

# Create a regex for valid input
# input string having set of 0,1 and * are acceptable else invalid
validation = re.compile(r"^[01*]+$")
while True:
    # Define input_string variable as sequence of strings.
    input_string = input("Please Enter Sequence of Digits.\n")

    # If input string matches regular expression
    if validation.match(input_string):
        # Append input to morse_code_list
        morse_code_list.append(input_string)

        # Define re_input variable to take the input again
        re_input = input("Do you want to input more? \nPress 'y' to enter more sequence or hit enter to Decode\n")
        # if 'y' take input again
        if re_input.lower() == 'y':
            True
        # Stop taking input
        else:
            break
    # if user input any string apart from 0, 1 , * . Reject the string
    else:
        print(input_string, "is invalid input")

# Convert list to string delimited by '*'
morse_code_string = '*'.join(morse_code_list)

# print valid morese code string
print("Original Message:", morse_code_string, "\n")
