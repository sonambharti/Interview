'''
Given an array arr[] of integers and an integer target. You mainly need to return the left and right 
indexes(1-based indexing) of that subarray, whose sum is equal to the given target. If there is no 
such subarray return [-1]
 
Input: arr[] = [1,2,3,7,5], target = 12
Output: [2, 4]
Explanation: The sum of elements from 2nd to 4th position is 12.
Input: arr[] = [1,2,3,4,5,6,7,8,9,10], target = 15,
Output: [1, 5]
Explanation: The sum of elements from 1st to 5th position is 15.

'''

def subarraySum(nums, target):
    n = len(nums)
    start, end = 0, 0 
    res = []
    
    curr = 0 
    
    for i in range(n):
        curr += nums[i]
        if curr >= target:
            end = i 
        
        while curr > target and start < end:
            curr -= nums[start]
            start += 1 
            
        if curr == target:
            res.append(start + 1)
            res.append(end + 1)
            return res 
    return [-1]
    
if __name__ == "__main__":
    nums = [1,2,3,7,5]
    target = 12
    
    print("The start and end indexes of the target sum subarray is: ", subarraySum(nums, target))
    print("The start and end indexes of the target sum subarray is: ", subarraySum([1,2,3,4,5,6,7,8,9,10], 15))
    
            
            
