"""
Given an Array A, find the minimum amplitude you can get after changing up to 3 elements. 
Amplitude is the range of the array (basically difference between largest and smallest element).

Example 1:

Input: [-1, 3, -1, 8, 5 4]
Output: 2
Explanation: we can change -1, -1, 8 to 3, 4 or 5

So the way I did it was sort it, and then start removing the end elements because we would 
only want to change a element to a number within the smallest amplitude. There are 4 options, 
remove all 3 from the end, remove 2 from end 1 from start, remove 1 from end and 2 from start, 
remove 3 from start.
"""

def min_amplitude(arr):
    arr.sort()
    n = len(arr)

    # Check for the case where we can remove 0, 1, 2, or 3 elements
    min_amp = min(arr[n-4] - arr[0], arr[n-3] - arr[1], arr[n-2] - arr[2], arr[n-1] - arr[3])

    return min_amp

# Example usage:
# input_arr = [-1, 3, -1, 8, 5, 4]
input_arr = [10, 10, 3, 4, 10]
output = min_amplitude(input_arr)
print("Output:", output)
