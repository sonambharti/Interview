"""
Given an array of integers. Find triplet in array which can sum to get the target. Return True if triplet found else return False.
"""

# Brute Force Approach
def tripletSum_Brute(arr, target):
    n = len(arr)
    for i in range(n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if arr[i] + arr[j] + arr[k] == target:
                    return True
    return False
    

def tripletSum(arr, target):
    n = len(arr)
    arr.sort()
    for i in range(n-2):
        left, right = i+1, n-1
        while left < right:
            s = arr[i] + arr[left] + arr[right]
            if s == target:
                return True
            elif s < target:
                left += 1 
            else:
                right -= 1
                
    return False
    
if __name__ == "__main__":
    arr = [3,12,9,7,5]
    target = 28
    
    res_B = tripletSum_Brute(arr, target)
    print("Brute Force Approach: ", res_B)
    
    res_O = tripletSum(arr, target)
    print("Optimize Approach: ", res_O)
    
