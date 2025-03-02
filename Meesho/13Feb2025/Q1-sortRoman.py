'''
# Ancestral Names

Given a list of strings comprised of a name and a Roman numeral, sort the list 
first by name, then by the decimal value of the Roman numeral.

In Roman numerals, a value is not repeated more than three times. At that point, 
a smaller value precedes a larger value to indicate subtraction. For example, 
the letter I represents the number 1, and Vrepresents 5. Reason through the formation
of 1 to 10 below, and see how it is applied in the following lines.

* I, II, III, IV, V, VI, VII, VIII, IX, and Xrepresent 1 through 10.

* XX, XXX, XL, and L are 20, 30, 40, and 50.

* For any other two-digit number <50, concatenate the Roman numeral(s) that represent 
its multiples of ten with the Roman numeral(s) for its values < 10. 
For example, 43 is 40 +3= 'XL' + 'II = 'XLIII'

Example

names = ['Steven XL', 'Steven XVI', 'David IX', 'Mary XV', 'Mary XIII', 'Mary XX']

The result with Roman numerals is the expected return value. Written in decimal and sorted, 
they are ['David 9', 'Mary 13', 'Mary 15', 'Mary 20', Steven 16', 'Steven 40'].

Function Description
Complete the function sortRoman in the editor below.

sortRoman has the following parameters:
names[n]: an array of strings comprised of names and roman numerals

Returns
string[n]: an array of strings sorted first by given name, then by ordinal.

Sample Input:
names = ['Louis IX', 'Louis VIII']

Output:
['Louis VIII', 'Louis IX']

'''


from typing import List, Tuple
import re

def roman_to_int(roman: str) -> int:
    roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total = 0
    prev_value = 0
    
    for char in reversed(roman):
        value = roman_values[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value
    
    return total

def parse_name_roman(entry: str) -> Tuple[str, int]:
    match = re.match(r"(\D+)\s+(\w+)", entry)
    if match:
        name, roman = match.groups()
        return name, roman_to_int(roman)
    return "", 0

def sort_names(names: List[str]) -> List[str]:
    return sorted(names, key=parse_name_roman)

if __name__ == "__main__":
    # Example usage
    # names = ["John X", "John II", "Alex V", "Alex III", "John I"]
    names = ['Louis IX', 'Louis VIII']
    sorted_names = sort_names(names)
    print(sorted_names)
