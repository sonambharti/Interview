'''
You are given an array of integers nums, there is a sliding window of size k
which is moving from the very left of the array to the very right. You can 
only see the k numbers in the window. Each time the sliding window moves 
right by one position.
Return the max sliding window.
 
Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]

'''

from collections import deque

def maxSliding_optimized(nums, k):
    # Complexity = O(nk)
    dq = deque()
    n = len(nums)
    res = []
    
    for i in range(n):
        while dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        dq.append(i)
        
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res
    
def maxSliding1(nums, k):
    # Complexity = O(nk)
    dq = deque()
    n = len(nums)
    res = []
    
    for i in range(n):
        dq.append(nums[i])
        if len(dq) > k:
            dq.popleft()
        if len(dq) == k:
            maxm = max(dq)
            res.append(maxm)
    return res

if __name__=="__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    
    
    ans = maxSliding1(nums, k)
    print("The maximum array: ",ans)
    
    ans1 = maxSliding_optimized(nums, k)
    print("The maximum array: ",ans1)
    
    
    
    
    
