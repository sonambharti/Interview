"""
write a python code to find the energy lost of a frog who wants to reach the 
last stair of stair case of length N. Height[i] is the height of (i+1) th stair.
If frog jump from ith to jth stair, the energy lost in the jump is given by 
absolute value of (Height[i-1] - Height[j-1]). If frog is on the ith staircase, 
he can jump either to (i+1)th stair or to (i+2)th stair. Find the minimum total 
energy used by frog to reach from 1st stair to Nth stair.
"""

def min_energy_lost(heights, n):
    
    dp = [float('inf')] * n

    # Base case: energy required to reach the 1st stair is 0.
    dp[0] = 0

    for i in range(n):
        # The energy required to reach the (i+1)th stair.
        if i + 1 < n:
            energy_to_i_plus_1 = dp[i] + abs(heights[i + 1] - heights[i])
            dp[i + 1] = min(dp[i + 1], energy_to_i_plus_1)

        # The energy required to reach the (i+2)th stair.
        if i + 2 < n:
            energy_to_i_plus_2 = dp[i] + abs(heights[i + 2] - heights[i])
            dp[i + 2] = min(dp[i + 2], energy_to_i_plus_2)

    return dp[n - 1]

# Test cases
heights = [7,4,4,2,6,6,3,4]
n = len(heights)
print("Minimum energy lost:", min_energy_lost(heights, n))  
