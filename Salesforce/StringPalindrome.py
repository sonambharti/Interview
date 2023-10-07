# String Palindrome

"""
Description: Given a  String s, return integer for count 
of all the unique palindromic, permutations of it. 
If s has no palindromic permutation, return 0.

s consists of only lowercase English letters.
"""

MAX = 2**8 

def factorial(num):
    if num==1 or num==0:
        return 1
        
    return num * factorial(num-1)
    
  
# Returns count of palindromic permutations of str.
def countPalinPermutations(s):
    global MAX
      
    # Count frequencies of all characters
    n = len(s)
    freq = [0] * MAX;
    for i in range(0, n) :
        freq[ord(s[i])] = freq[ord(s[i])] + 1;
        
    # Since half of the characters decide count of palindromic permutations, we take (n/2)!
    res = factorial(n // 2)
  
    # To make sure that there is at most one odd occurring char
    oddFreq = False
  
    # Traverse through all counts
    for i in range(0, MAX) :
        half = freq[i] // 2
  
        # To make sure that the string can permute to form a palindrome
        if (freq[i] % 2 != 0):
  
            # If there are more than one odd occurring chars
            if (oddFreq == True):
                return 0
            oddFreq = True
  
        # Divide all permutations with repeated characters
        res = (res%1000000007) // factorial(half)
  
    return res
    
if __name__ == "__main__":
    s = input("Enter the string: ")
    res = countPalinPermutations(s)
    print("Output \nCount of all possible palindromic permutations: ", res)
