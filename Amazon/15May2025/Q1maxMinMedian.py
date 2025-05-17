"""
# Q1
A new Amazon intern encountered a challenging tank Currently, the intern has in integers, where the
salue of the element is represented by the array element values(il
The intern is curious to play with arrays and subsequences and thus asks you to join him.
Given n integer, array values, and an integer & the intern needs to find the maximum and minimum median 
overall subsequences of length.k

Example:
Given n = 3, values = [1,2,3] and k=2.

|Subsequences of length k   |   median   |
|[1, 2]                     |       1    |
|[1, 3]                     |       1    |
|[2, 3]                     |       2    |

Here, the maximum median present is 2 and the minimum median in the subsequence present is 1.

#   Function Description
Complete the function medians in the editor below. medians has the following parameter(s)
int valuering the value of integers
int k the given integer

#   Returns 
int[]: the maximum and minimum overall tubsequences of length & in the form [maximum median, minimum median)

Sample Case:

Input 1: values = [56, 21]; k = 1 
Output: [56, 21]

Input 2: values = [16, 21, 9, 2, 78]; k = 5 
Output: [16, 16]


"""

def medians(values, k):
    sorted_vals = sorted(values)

    # Minimum median comes from smallest k elements
    min_sub = sorted_vals[:k]
    min_median = min_sub[(k - 1) // 2]

    # Maximum median comes from largest k elements
    max_sub = sorted_vals[-k:]
    max_median = max_sub[(k - 1) // 2]

    return [max_median, min_median]


if __name__ == "__main__":
    values = [16, 21, 9, 2, 78]
    k = 5
    
    res = medians(values, k)
    print(f"The maximum and minimum overall subsequences of length & in the form [maximum median, minimum median): {res}")
