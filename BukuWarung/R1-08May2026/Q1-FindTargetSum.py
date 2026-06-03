"""
write python code to find 2 numbers from an integer array to get a target sum.
"""

def two_sum_bruteforce(nums, target):
    # Time Complexity: O(n^2)
    # Space Complexity: O(1)
    n = len(nums)

    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)

    return None

def two_sum_sorted_2pointers(nums, target):
    # Time Complexity: O(nlog n)
    # Space Complexity: O(n)
    nums = sorted(nums)
    left = 0
    right = len(nums) - 1

    while left < right:
        curr_sum = nums[left] + nums[right]

        if curr_sum == target:
            # return (nums[left], nums[right])
            return (left, right)

        elif curr_sum < target:
            left += 1

        else:
            right -= 1

    return None


def two_sum(nums, target): 
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    
    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return (seen[complement], i)

        seen[num] = i

    return None
    
if __name__ == "__main__":
    nums = [2, 7, 15, 11]
    target = 9
    
    print("Brute force: ", two_sum_bruteforce(nums, target))
    print("Optimized: ", two_sum(nums, target))
    print("2 pointers: ", two_sum_sorted_2pointers(nums, target))
