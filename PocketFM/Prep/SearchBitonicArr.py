'''
Given a bitonic sequence of n distinct elements, and an integer x, 
the task is to write a program to find given element x in the bitonic 
sequence in O(log n) time. 

A Bitonic Sequence is a sequence of numbers that is first strictly increasing then after a point decreasing.

Example 1:
Input: arr[] = {-3, 9, 18, 20, 17, 5, 1}, key = 20
Output: Found at index 3

'''

def find_BitonicPoint(arr, n, left, right): 
    bitonicPoint = 0
    mid = (left + right)//2
    if arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
        return mid
    elif arr[mid] > arr[mid-1] and arr[mid] < arr[mid+1]:
        bitonicPoint = findBitonicPoint(arr, n, mid, right)
    else:
        bitonicPoint = finsBitonicPoint(arr, n, left, mid)
         
    return bitonicPoint
    
def ascend_BinarySearch(arr, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            right = mid-1
        else:
            left = mid+1
    return -1
    
def descend_BinarySearch(arr, left, right, key):
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            right = mid-1
        else:
            left = mid+1
    return -1
    
def Search_BitonicArr(arr, n, key, index):
    if arr[index] == key:
        return index
    elif arr[index] > key:
        return -1
    else:
        temp = ascend_BinarySearch(arr, 0, index, key)
        if temp != -1:
            return temp
        return descend_BinarySearch(arr, index-1, n, key)
        
        
    
    
   
if __name__ == "__main__":
    print("A Bitonic Sequence is a sequence of numbers that is \
    first strictly increasing then after a point decreasing.")
    nums = [-3, 9, 18, 20, 17, 5, 1]
    key = 20
    n = len(nums)
    Bitonic_indx = find_BitonicPoint(nums, n, 0, n-1)
    print("Find key at: ", Search_BitonicArr(nums, n, key, Bitonic_indx))
    Sea
