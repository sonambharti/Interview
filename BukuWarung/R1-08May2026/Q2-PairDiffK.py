'''
# Pair with Difference K

You are given a sorted list of integers arr (ascending order, may contain duplicates) and a non-negative integer k. 
Your task is to find any pair of indices (i, j) with i < j such that arr[j] - arr[i] == k.
Return the pair as a tuple (i, j). If no such pair exists, return None.

Examples:
find_pair_with_diff([1, 5, 8, 11, 15], k=7)   ->  (1, 3)   # arr[3] - arr[1] = 11 - 5 = 7
find_pair_with_diff([3, 7, 9, 12, 16], k=5)   ->  (1, 3)   # arr[3] - arr[1] = 12 - 7 = 5
find_pair_with_diff([1, 1, 2, 3], k=0)        ->  (0, 1)   # duplicates count
find_pair_with_diff([1, 2, 3], k=10)          ->  None
find_pair_with_diff([], k=5)                  ->  None
find_pair_with_diff([4], k=0)                 ->  None     # need two elements
Constraints:
0 ≤ len(arr) ≤ 10^5
-10^9 ≤ arr[i] ≤ 10^9
k ≥ 0 (non-negative)
arr is sorted in ascending order on input. You may assume this.
If multiple valid pairs exist, return any one.
'''

# def pairWithDiff(arr, k):
#     n = len(arr) # n = 5
#     left, right = 0, 1 # left = 0, right = 4
    
#     while left < n and right < n: # 2 < 4
#         if left == right:
#             right += 1
#             continue
#         val = arr[right] - arr[left] # 15 - 8 = 7
#         if val == k:
#             return (left, right)
#         elif val > k: # 10 > 7
#             left += 1 # left = 2
#         elif val < k:
#             right -= 1
#     return (-1,-1)
    
    
def pairWithDiff(arr, k):
    n = len(arr)

    left, right = 0, 1

    while right < n and left < n:

        # avoid same element to maintain uniqueness
        if left == right:
            right += 1
            continue

        val = arr[right] - arr[left]

        if val == k:
            return (left, right)

        elif val < k:
            right += 1

        elif val > k:
            left += 1

    return (-1, -1)


def allPairsWithDiff(arr, k):
    n = len(arr)

    left = 0
    right = 1

    result = []

    while right < n and left < n:

        if left == right:
            right += 1
            continue

        diff = arr[right] - arr[left]

        if diff == k:
            result.append((left, right))

            # move both to continue searching
            left += 1
            right += 1

        elif diff < k:
            right += 1

        else:
            left += 1

    return result


if __name__ == "__main__":
    # arr = [1, 5, 8, 12, 20]
    arr = [1, 5, 8, 11, 15]
    k = 7
    left, right = pairWithDiff(arr, k)
    print(f"left = {left}, right = {right}")
    
    print(f"All pairs of indexes: {allPairsWithDiff(arr, k)}")
