'''
Given a string, return the length of substring which do not have duplicate characters.

Input
abcabcbb
output: 3
'''

def length_of_longest_substr_brute(s): # O(n^2)
    n = len(s)
    max_len = 0
    
    for i in range(n):
        seen = set()
        for j in range(i, n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j-i+1)
    return max_len


def length_of_longest_substr_opt(s):
    seen = {} # hash map
    max_len = 0
    left = 0
    
    for right, char in enumerate(s):
        if char in seen and seen[char] >= left:
            left = seen[char] + 1 
        seen[char] = right
        max_len = max(max_len, right-left+1)
    return max_len
        

if __name__ == "__main__":
    s = "abcabcbb"
    res = length_of_longest_substr_brute(s)
    print("Length of unique characters: ", res)
    
    
    res_opt = length_of_longest_substr_opt(s)
    print("Length of longest substr with unique chars: ", res_opt)
    
    arr = ["abcabcdb","a","aaaaaa","abcdefg","abccbdefba","aabcdefg"]
    
    for s1 in arr:
        ans = length_of_longest_substr_opt(s1)
        print("Longest Unique chars: ", ans)
