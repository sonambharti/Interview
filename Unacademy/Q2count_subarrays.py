'''
# Q2. Not More than K times

Count the no of subarrays in an array of size N where none of the elements occur more than a given number of times.

Examples:
Input:
N = 5
nums = [1, 2, 1, 3, 1]
K = 1
Output: 10
'''

from collections import defaultdict

def count_subarrays(N, nums, K):

    start = 0
    freq = defaultdict(int)
    count = 0

    for end in range(N):
        # Include nums[end] in the window
        freq[nums[end]] += 1

        # Shrink the window if any element's count exceeds K
        while freq[nums[end]] > K:
            freq[nums[start]] -= 1
            if freq[nums[start]] == 0:
                del freq[nums[start]]
            start += 1

        # All subarrays ending at 'end' and starting from 'start' are valid
        count += end - start + 1

    return count

if __name__ == '__main__':
    N = 5
    nums = [1, 2, 1, 3, 1]
    K = 1
    print(count_subarrays(N, nums, K))
	
