'''
# Maximimize the Beauty of Array

The beauty of a n array a of length m is defined as the number of integers i(1 <= i <= m) such that a[i]= 1.
Given an array of n integers, the following operation can be performed on the array while its length is greater than 1.
- Choose some i (1<=i<=length of array) and delete arr[i] without changing order of the remaining elements.
Find the maximum possible beauty of the array after performing this operation any number of times.

Example
n = 7
arr = [1, 3, 2, 5, 4, 5, 3] 
One optimal sequence of operations as shown.
- Choose i=2, delete arr[2] = 3; arr = [1, 2, 5, 4, 5, 3] 
- Choose i=6, delete arr[6] = 3; arr = [1, 2, 5, 4, 5] 

The beauty of arr is 4 since arr[1] = 1, arr[2] = 2, arr[4] = 4 and arr[5] = 5.

Return 4.

Sample Input 1:
n = 6
arr = [6, 3, 2, 4, 3, 4]

Sample Output 1: 3

Sample Input 2:
n = 4
arr = [3, 2, 1, 2]

Sample Output 2: 2


'''

def maximizeBeauty(arr):
    n = len(arr)
    # Initialize DP array
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # If we don't include the current element, the beauty remains the same as dp[i-1]
        dp[i] = dp[i - 1]
        
        # If we include the current element, check if it can contribute to the beauty
        # The current element is arr[i-1] (0-based index)
        if arr[i - 1] <= i and arr[i - 1] >= 1:
            # If we include this element, the beauty increases by 1
            dp[i] = max(dp[i], dp[arr[i - 1]] + 1)
    
    return dp[n]



if __name__ == "__main__":
    # Example usage
    arr1 = [1, 3, 2, 5, 4, 5, 3]
    print(maximizeBeauty(arr1))  # Output: 4
    
    arr2 = [6, 3, 2, 4, 3, 4]
    print(maximizeBeauty(arr2))  # Output: 3
    
    arr3 = [3, 2, 1, 2]
    print(maximizeBeauty(arr3))  # Output: 2
