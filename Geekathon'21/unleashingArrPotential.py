# Unleashing the array potential.

"""
Given an array arr[ ] consisting of n integers, find the maximum Geek Value of 
the array to unleash its true potential. 

Geek value is defined as (arri - arrj) × arrk, where 1 ≤ i < j < k ≤ n.

Please note that if the Geek Value turns out to be negative, return 0 as the answer. 

Example:

Input :
n = 5
arr = {10,1,4,2,7}
Output:
63  
Explanation:
Take indices i=1,j=2 and k=5 {one based indexing} 
Geek value = (arr[1]−arr[2])×arr[5] = 63.

"""

def solver(arr, n):
    
    # Brute Force approach...
    
    # res = -2**63-1
    
    # for i in range(n):
    #     for j in range(i+1, n):
    #         for k in range(j+1, n):
    #             mid_res = (arr[i] - arr[j]) * arr[k]
                
    #             res = max(mid_res, res)
    

    #     if res < 0:
    #         return 0
            
    suff = [0]*n
    for i in range(n-2,-1,-1):
        suff[i] = max(suff[i+1], arr[i+1])
            
    prefMax = arr[0]
    res = 0
    
    for j in range(1, n-1):
       res = max(res, (prefMax - arr[j]) * suff[j]) 
       prefMax = max(prefMax, arr[j])
    
        
    return res
        

    
arr = [9, 3, 2, 5]
n = len(arr)
print(solver(arr,n))
