#######################################Task3#############################################
#                           Name: Shubhank Vijayvergiya                                 #
#                           Student Id: 29421934                                        #
#                           Start Date: 22/03/2018                                      #
#                           Last Modified Date: 28/03/2018                              #
#######################################Task3#############################################



'''
Description:
Decode morse_code_string with the help of morse_code_dictionary. Store valid characters in valid_characters_list
and invalid characters in invalid_characters_list.
print valid decoded characters and invalid characters.
'''

# import dictionary defined in Task1
from Task1 import morse_code_dictionary
# import input string from Task2
from Task2 import morse_code_string

# split input string, delimited by '*', and store in morse_code_list variable
morse_code_list = morse_code_string.split("*")

# Define length_of_list variable, storing length of morse_code_list
length_of_list = len(morse_code_list)

# Initialize traverse_list variable with 0
traverse_list = 0

# Define a list for valid characters in morse code input string
valid_characters_list = []

# Define a list for invalid characters in morse code input string
invalid_characters_list = []

# while traverse_list is less then length_of_list variable is True
while traverse_list < length_of_list:
    # If morse_code_list is present in morse_code_dictionary
    if morse_code_list[traverse_list] in morse_code_dictionary:
        # Decode string in morse_code_list with the help of morse_code_dictionary
        # Append the decoded string to valid_characters_list
        valid_characters_list.append(morse_code_dictionary[morse_code_list[traverse_list]])
    # If morse_code_list is NOT present in morse_code_dictionary
    else:
        # Append invalid string to invalid_characters_list
        invalid_characters_list.append(morse_code_list[traverse_list])
    # Increment traverse_list value with 1
    traverse_list += 1

# If length of valid_characters_list is greater than 0
if len(valid_characters_list) > 0:
    # Convert list of characters to string and print
    print("Translated Message:", ''.join(valid_characters_list).lower(), "\n")
# If length of invalid_characters_list is greater than 0
if len(invalid_characters_list) > 0:
    # Convert list of characters to string and print
    print(','.join(invalid_characters_list), "is/are invalid character/s.", "\n")
