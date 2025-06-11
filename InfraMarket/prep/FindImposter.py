'''
# Find the Imposter in a Sorted Array
You are given a sorted array a consisting of integers where every element appears exactly
twice, except one element which appears only once. Your task is to find and return that 
single element (the imposter).

Your solution should have:
Time Complexity: O(log n)
Space Complexity: O(1)

Example:

Input: a = [1, 1, 2, 2, 4, 5, 5, 6, 6]
Output: 4
Explanation:
All elements appear twice: 1, 2, 5, 6
The only element that appears once is 4, which is the answer.

Constraints:
The array is sorted in non-decreasing order.
The length of the array is 2n + 1 for some integer n (i.e., always odd).
Only one element appears once; all others appear exactly twice.
'''
# Brute Force - O(n)
def findImposter_XOR(arr):
    res = 0
    for el in arr:
        res^=el 
    return res
    
# Optimized - O(log n)
def findImposter_Binry(arr):
    n = len(arr)
    left = 0
    right = n-1
    
    while(left < right):
        mid = left + (right - left) // 2 
        if (mid - 1) > 0 and (arr[mid] == arr[mid - 1]):
            right = mid - 2 
        if (mid - 1) > 0 and (arr[mid] == arr[mid + 1]):
            left = mid + 2 
        else:
            return arr[mid]
    return arr[left]

if __name__ == "__main__":
    arr = [1, 1, 2, 2, 4, 5, 5, 6, 6]
    print(f'Using XOR op: ', findImposter_XOR(arr))
    print(f'Using Binary Search: ', findImposter_Binry(arr))
    
    
