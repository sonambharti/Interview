'''
# Minimum Days to Make n Bouquets

You are given an unsorted integer array bloomDay, where each element represents the day on which a 
specific flower will bloom.

You are also given two integers:
n → the number of bouquets you need to make
k → the **number of adjacent flowers required to make one bouquet

Your task is to find the minimum number of days required to make n bouquets, where each bouquet 
consists of exactly k adjacent bloomed flowers.

If it's not possible to make n bouquets, return -1.

Example:
Input:
bloomDay = [1, 10, 3, 10, 2]
n = 3
k = 1

Output:
3
Explanation:
By day 3, the flowers at indices 0, 2, and 4 will bloom.
We can pick 3 single flowers (each bouquet of size 1) → total 3 bouquets made.

Example 2:
Input:
bloomDay = [1, 10, 3, 10, 2]
n = 3
k = 2

Output:
-1
Explanation:
We need 3 bouquets of 2 adjacent bloomed flowers.
But even on day 10, there's no way to group them into 3 such adjacent pairs.

Constraints:
1 <= bloomDay.length <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= n <= 10^6
1 <= k <= bloomDay.length
'''

"""
If bloomDay is sorted then we can directly check (n*k) th index that ll return the no. of days....
"""

def is_possible(bloomDay, day, n, k):
    bouquets = 0
    flowers = 0
    for b in bloomDay:
        if b <= day:
            flowers += 1
            if flowers == k:
                bouquets += 1
                flowers = 0
        else:
            flowers = 0
    return bouquets >= n

def min_days_brute(bloomDay, n, k):
    if n * k > len(bloomDay):
        return -1

    for day in range(1, max(bloomDay)+1):
        if is_possible(bloomDay, day, n, k):
            return day
    return -1


def min_days_optimized(bloomDay, n, k):
    if n * k > len(bloomDay):
        return -1
    
    low, high = min(bloomDay), max(bloomDay)
    ans = -1
    
    while low <= high:
        mid = (low + high) // 2
        if is_possible(bloomDay, mid, n, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    
    return ans
    
if __name__ == "__main__":
    # bloomDay = [1, 10, 3, 10, 2]
    # n = 3
    # k = 2
    bloomDay = [1, 10, 3, 10, 2]
    n = 3
    k = 1
    print(f'Brute Force Approach: ', min_days_brute(bloomDay, n, k))
    print(f'Optimized Approach: ', min_days_optimized(bloomDay, n, k))
