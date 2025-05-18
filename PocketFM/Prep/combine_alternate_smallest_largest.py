"""
#  Combine Alternate Smallest Largest Nos in an array

Given two sorted arrays, combine them such that the first element is the smallest,
the second is the largest, and so on.
"""

def brute_combine_alternate_smallest_largest(arr1, arr2):   # Complexity: O(log(n+m).(n+m))
    # Merge the arrays
    merged = sorted(arr1 + arr2)
    
    # Initialize result list
    result = []

    # Use two pointers: one from the start (smallest), one from the end (largest)
    left, right = 0, len(merged) - 1

    # Alternate appending smallest and largest
    toggle = True
    while left <= right:
        if toggle:
            result.append(merged[left])
            left += 1
        else:
            result.append(merged[right])
            right -= 1
        toggle = not toggle

    return result
    
    
def combine_alternate_smallest_largest(arr1, arr2):
    # Merge two sorted arrays manually in O(n + m)
    i = j = 0
    merged = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1
    while i < len(arr1):
        merged.append(arr1[i])
        i += 1
    while j < len(arr2):
        merged.append(arr2[j])
        j += 1

    # Rearranging in smallest-largest-alternate pattern
    result = []
    left, right = 0, len(merged) - 1
    toggle = True
    while left <= right:
        if toggle:
            result.append(merged[left])
            left += 1
        else:
            result.append(merged[right])
            right -= 1
        toggle = not toggle

    return result


if __name__ == "__main__":
    # Example usage
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    print("Brute Force Approach: ", brute_combine_alternate_smallest_largest(arr1, arr2))
    print("Optimized Approach: ", combine_alternate_smallest_largest(arr1, arr2))
