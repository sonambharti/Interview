"""
#   Maximum Sum path in two arrays

Given two arrays arr1 and arr2. First sort both the arrays. The arrays may have some common elements.
Find the sum of the maximum sum path to reach from the beginning of any array to the end of any of the 
two arrays. You can start from any array and switch from one array to another array only at common elements. 

Examples:

Input: arr1[] = [2, 3, 7, 10, 12] and arr2[] = [1, 5, 7, 8]
Output: 35
Explanation: 35 is sum of 1 + 5 + 7 + 10 + 12. We start from the first element of arr2 which is 1, then
we move to 5, then 7 From 7, we switch to arr1 (as 7 is common) and traverse 10 and 12.

Input: arr1[] = [10, 12] and arr2[] = [5, 7, 9]
Output: 22
Explanation: 22 is the sum of 10 and 12. Since there is no common element, we need to take all elements 
from the array with more sum.

Expected Time Complexity: O(nlogn)
Expected Auxiliary Space: O(1)
"""

def maxPathSum(arr1, arr2):
    # Step 1: Sort both arrays
    arr1.sort()
    arr2.sort()
    
    i = j = 0
    sum1 = sum2 = result = 0
    n, m = len(arr1), len(arr2)

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            sum1 += arr1[i]
            i += 1
        elif arr1[i] > arr2[j]:
            sum2 += arr2[j]
            j += 1
        else:
            # Common element
            result += max(sum1, sum2) + arr1[i]
            sum1 = sum2 = 0
            i += 1
            j += 1

    # Add remaining elements
    while i < n:
        sum1 += arr1[i]
        i += 1
    while j < m:
        sum2 += arr2[j]
        j += 1

    result += max(sum1, sum2)
    return result
    
if __name__ == "__main__":
    arr1 = [2, 3, 7, 10, 12] 
    arr2 = [1, 5, 7, 8]
   
    res = maxPathSum(arr1, arr2)
    
    print("Maximum Sum in given arrays = ", res)
  
