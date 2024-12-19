"""
Find the power of a number to n.

Example:
Input:
num = 4, n = 5
Output:
1024
"""

def power_Brute(x, n):
    res = 1
    for i in range(n):
        res *= x 
    return res
    
def power(x, n):
    #Complexity: O(log n)
    res = 1 
    while n:
        lastBit = n&1 
        if lastBit:
            res *= x 
        x *= x
        n >>= 1 
    return res
    
if __name__ == "__main__":
    num = 4
    n = 5
    print("Brute Force approach to find power: ", power_Brute(num, n))
    print("Bit mask approach to find power: ", power(num, n))
