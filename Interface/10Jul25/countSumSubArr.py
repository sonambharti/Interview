'''
Given a array of integers(positive, negative, 0), 
given a value k return the number of subarrays which sum upto k.

Input: nums = [1, 1, 1], k = 2  
Output: 2
'''

def count_sub_arr_brute(arr, k): # n^2
    n = len(arr)
    count = 0
    
    for i in range(n):
        currSum = 0
        for j in range(i, n):
            currSum += arr[j]
            
            if currSum == k:
                count += 1 
    return count
    
    
def count_sub_arr_opt(arr, k):
    prefixSum = {}
    count = 0
    currSum = 0
    
    for val in arr:
        currSum += val
        if currSum == k:
            count += 1 
        if currSum - k in prefixSum:
            count += prefixSum[currSum - k]
        
        prefixSum[currSum] = prefixSum.get(currSum, 0) + 1 
    return count
    



if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    res = count_sub_arr_brute(nums, k)
    print("The no of subarrays with k sum: ", res)
    
    res_opt = count_sub_arr_opt(nums, k)
    print("The no of subarrays with k sum in opt: ", res_opt)
    
    test = [0, 1, 0, 1, 0]
    k1 = 1
    ans = count_sub_arr_opt(test, k1)
    print(ans)

    
