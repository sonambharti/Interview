'''
Question 2:
Given a string S, we can split S into 2 strings: S1 and S2. 
Return the number of ways S can be split such that the number 
of unique characters between S1 and S2 are the same.

Example 1:

Input: "aaaa"
Output: 3
Explanation: we can get a - aaa, aa - aa, aaa- a

'''

def count_ways_to_split(s):
    n = len(s)
    unique_chars = set()
    count = 0

    for i in range(1, n):
        unique_chars.add(s[i - 1])

        if len(unique_chars) == len(set(s[i:])):
            count += 1

    return count

# Example usage:
# input_str = "aaaa"
input_str = "bac"
output = count_ways_to_split(input_str)
print("Output:", output)
