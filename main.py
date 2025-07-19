# This a python password generator
# Import randon 
import string

def generate_password(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special =string.punctuation
    

    characters = letters
    if numbers :
        characters += digits
    if special_characters :
        characters += special

        pwd =""
        


generate_password(10)