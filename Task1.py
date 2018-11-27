#######################################Task1#############################################
#                           Name: Shubhank Vijayvergiya                                 #
#                           Student Id: 29421934                                        #
#                           Start Date: 22/03/2018                                      #
#                           Last Modified Date: 27/03/2018                              #
#######################################Task1#############################################

"""
Description:
morse_code_dictionary represent each of the Morse code characters from 'A' to 'Z' and '0' to '9'.
In below morse_code_dictionary the 'dots' are represented by the digit 0 and the 'dashes' are
represented by the digit '1' and the spaces are represented by the character '*'
"""

# Define morse code dictionary as key-value pair.
morse_code_dictionary = {"01": "A"
    , "1000": "B"
    , "1010": "C"
    , "100": "D"
    , "0": "E"
    , "0010": "F"
    , "110": "G"
    , "0000": "H"
    , "00": "I"
    , "0111": "J"
    , "101": "K"
    , "0100": "L"
    , "11": "M"
    , "10": "N"
    , "111": "O"
    , "0110": "P"
    , "1101": "Q"
    , "010": "R"
    , "000": "S"
    , "1": "T"
    , "001": "U"
    , "0001": "V"
    , "011": "W"
    , "1001": "X"
    , "1011": "Y"
    , "1100": "Z"
    , "11111": "0"
    , "01111": "1"
    , "00111": "2"
    , "00011": "3"
    , "00001": "4"
    , "00000": "5"
    , "10000": "6"
    , "11000": "7"
    , "11100": "8"
    , "11110": "9"
    }


print("MORSE CODE", "\t"*3, "CHARACTER", "\n")
# print Morse code dictionary along with keys and values
for pair in morse_code_dictionary:
    print(pair.ljust(3), "\t"*5, morse_code_dictionary.get(pair))

