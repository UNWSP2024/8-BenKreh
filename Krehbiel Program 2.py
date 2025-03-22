#Ben Krehbiel
#3/17/2025
#Split the name

import re

def get_name():
    name = input("Please enter your first name, middle initial, and last name: ")
    name_separated = re.findall(r'[A-Z][a-z]*', name)
    print(name_separated)

get_name()
