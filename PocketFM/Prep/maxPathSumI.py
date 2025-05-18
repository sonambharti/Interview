"""
# Max Sum Path

Given two sorted arrays of distinct integers arr1 and arr2. Each array may have some 
elements in common with the other array. Find the maximum sum of a path from the 
beginning of any array to the end of any array. You can switch from one array to 
another array only at the common elements.

Note:  When we switch from one array to other,  we need to consider the common element 
only once in the result.

Examples : 

Input: arr1 = [2, 3, 7, 10, 12] , arr2 = [1, 5, 7, 8]
Output: 35
Explanation: The path will be 1+5+7+10+12 = 35, where 1 and 5 come from arr2 and then 7 
is common so we switch to arr1 and add 10 and 12.

Input: arr1 = [1, 2, 3] , arr2[] = [3, 4, 5]
Output: 15
Explanation: The path will be 1+2+3+4+5=15.


Expected Time Complexity: O(m + n)
Expected Auxiliary Space: O(1)

"""


def maxPathSum(arr1, arr2):
    # Code here
    sum1, sum2 = 0, 0
    n = len(arr1)
    m = len(arr2)
    
    i, j = n-1, m-1
    
    while i>=0 and j>=0:
        if arr1[i] > arr2[j]:
            sum1 += arr1[i]
            i -= 1
        if arr2[j] > arr1[i]:
            sum2 += arr2[j]
            j -= 1
        if arr1[i] == arr2[j]:
            if sum1 > sum2:
                sum1 += arr1[i]
                sum2 = sum1
            else:
                sum2 += arr2[j]
                sum1 = sum2
            i -= 1
            j -= 1
    
    while i >= 0:
        sum1 += arr1[i]
        i -= 1
        
    while j >= 0:
        sum2 += arr2[j]
        j -= 1
        
    return max(sum1, sum2)
        
if __name__ == "__main__":
    arr1 = [2, 3, 7, 10, 12] 
    arr2 = [1, 5, 7, 8]
   
    res = maxPathSum(arr1, arr2)
    
    print("Maximum Sum in given arrays = ", res)
  
