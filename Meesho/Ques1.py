##Packaging System

"""
An automated packaging system is reponsible for packing boxes. A box is certified to 
hold a certain weight. Given an integer total, calculate the no. of possible ways to 
achieve total as a sum of the weights of items weighing integer weights from 1 to k, inclusive.
"""

# Function that returns the number of ways to sum
# to N using natural numbers up to K with repetitions allowed


# def number_of_ways(N, K):
#    TLE error
# 	# Base case
# 	if N == 0:
# 		return 1
# 	if N < 0 or K <= 0:
# 		return 0

# 	# Including and not including K in sum
# 	return number_of_ways(N - K, K) + number_of_ways(N, K - 1)

def NumberOfways(N, K):
   
    # Initialize a list
    dp = [0] * (N + 1)
     
    # Update dp[0] to 1
    dp[0] = 1
     
    # Iterate over the range [1, K + 1]
    for row in range(1, K + 1):
        # Iterate over the range [1, N + 1]
        for col in range(1, N + 1):
           
            # If col is greater
            # than or equal to row
            if (col >= row):
                # Update current
                # dp[col] state
                dp[col] = dp[col] + dp[col - row]
                 
                 
    # Return the total number of ways
    return(dp[N])
  
# Driver code
if __name__ == '__main__':
	N = 8
	K = 2

	# Function call
	print(number_of_ways(N, K))
