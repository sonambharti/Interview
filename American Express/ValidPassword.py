"""
write a python code to check if a string is valid or not. The conditions to be true string are:
1. length of the string must be between (8-15) characters.
2. at least one digit (0-9), one lower case (a-z), one upper case (A-Z0 and one special character (%, ^, &, #, *, etc) must be present.
3. string must not contain any space.

"""


import re

def is_valid_string(s):
    # Condition 1: Length of the string must be between 8 and 15 characters.
    if not 8 <= len(s) <= 15:
        return False

    # Condition 2: Check if at least one digit, one lower case letter,
    # one upper case letter, and one special character are present.
    if not re.search(r"\d", s) or not re.search(r"[a-z]", s) or not re.search(r"[A-Z]", s) or not re.search(r"[!@#$%^&*()_+{}|:\"<>?`\-=[\]\\;',./]", s):
        return False

    # Condition 3: Check if the string contains any spaces.
    if " " in s:
        return False

    return True

test_string = input()

if is_valid_string(test_string):
    print("Valid")
else:
    print("Not Valid")

