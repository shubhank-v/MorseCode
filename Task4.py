#######################################Task4#############################################
#                           Name: Shubhank Vijayvergiya                                 #
#                           Student Id: 29421934                                        #
#                           Start Date: 22/03/2018                                      #
#                           Last Modified Date: 28/03/2018                              #
#######################################Task4#############################################

'''
Description:
Storing the number of occurrence of decoded characters in alphabet_counter_list variable. Zipping alphabet_list
and alphabet_counter_list and printing result on console.
'''

from Task3 import *

# Initialize traverse_list2 variable with 0
traverse_list2 = 0

# Define a list for 26 letters and 10 numerals
alphabets_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'
    , 't', 'v', 'u', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Define a list for the count of 26 letters and 10 numerals
alphabet_counter_list = [0] * 36

# while traverse_list2 is less then length_of_list variable is True
while traverse_list2 < length_of_list:
    # If morse_code_list is present in morse_code_dictionary
    if morse_code_list[traverse_list2] in morse_code_dictionary:
        # Store decode value of character in alphabet
        for alphabet in morse_code_dictionary[morse_code_list[traverse_list2]].lower():
            # Check decoded alphabet in alphabets_list
            if alphabet.lower() in alphabets_list:
                # Find index of alphabet in alphabets_list
                # Increment alphabet_counter_list with 1
                alphabet_counter_list[alphabets_list.index(alphabet)] += 1
    # Increment traverse_list2 value with 1
    traverse_list2 += 1
# Zip alphabets_list and alphabet_counter_list
zippedTuple = zip(alphabets_list, alphabet_counter_list)

# Create new dictionary from the tuple
character_count = dict(list(zippedTuple))

for count in character_count:
    print("Character ", count, "has", character_count.get(count), " occurrences.")
