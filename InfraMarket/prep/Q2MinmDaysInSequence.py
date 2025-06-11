'''
# Minimum Days to Make n Bouquets (Sequential Plucking Constraint) - Follow Up of 1st question
You are given an unsorted array bloomDay, where bloomDay[i] represents the day on which the flower 
at index i will bloom.

You are also given:

n → number of bouquets to make
k → number of adjacent flowers required per bouquet

🛑 New Constraint:

You cannot pluck any flower at position i until all previous flowers (0 to i-1) have been plucked —
i.e., you must pluck flowers in order from left to right.

Return the minimum number of days required to make n bouquets, where each bouquet contains exactly 
k adjacent bloomed flowers, and all flowers before index i must be plucked before plucking flower i.

If it's not possible, return -1.

Example:
Input:
bloomDay = [1, 10, 3, 10, 2]
n = 2
k = 2

Output:
10
Explanation:
You must pluck flowers from left to right.
By day 10, the bloomDay becomes: [1✓, 10✓, 3✓, 10✓, 2✓]
Valid bouquets possible: [1,10] and [3,10] — both adjacent and sequentially plucked.

Constraints:
1 <= bloomDay.length <= 10^5
1 <= bloomDay[i] <= 10^9
1 <= n <= 10^6
1 <= k <= bloomDay.length
'''
def canMakeBouquets(bloomDay, day, n, k):
    count = 0
    flowers = 0
    for i in range(len(bloomDay)):
        if bloomDay[i] <= day:
            flowers += 1
            if flowers == k:
                count += 1
                flowers = 0
                if count == n:
                    return True
        else:
            flowers = 0  # reset since we need k adjacent bloomed flowers
    return count >= n
        

def minDaysSequentialBouquets(bloomDay, n, k):
    if n * k > len(bloomDay):  # not enough flowers
        return -1

    low, high = min(bloomDay), max(bloomDay)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if canMakeBouquets(bloomDay, mid, n, k):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans

if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    n = 2
    k = 2
    print(minDaysSequentialBouquets(bloomDay, n, k))
    
    
    
