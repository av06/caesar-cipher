#!/usr/bin/env python3
"""This script prompts a user to enter a message to encode or decode
using a classic Caesar shift substitution (3 letter shift)"""

import string

shift = 3 #to store Caesar shift value
choice = input("would you like to encode or decode?\n") #checks the choice of user
word = input("Please enter text\n") #input text from user to encode/decode
if type(word) not in [str]:
    raise TypeError("The entered word should be a valid string!")
#raises exception if the entered word is not a string

letters = string.ascii_letters + string.punctuation + string.digits
encoded = ''
if choice == "encode": #encoding logic
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) + shift
            encoded = encoded + letters[x]
if choice == "decode": #decoding logic
    for letter in word:
        if letter == ' ':
            encoded = encoded + ' '
        else:
            x = letters.index(letter) - shift
            encoded = encoded + letters[x]

print encoded #prints the encoded/decoded output
