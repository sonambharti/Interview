""" 
# Q2
Given a list of n delivery zones, where the 4th zone covers the interval(a[I], b[I])(inclusive). Additionally, given is a maximum allowed 
length k, for any new delivery zone that can be added.
Your task is to add exactly one new delivery zone(a, b) such that the length of this new zone (b-a) is less than or equal to k. The goal
is to minimise the number of disconnected delivery zones after adding the new delivery zone.

A set of delivery zones [(a[1], b[1]), (a[2], b[2]), ..., (a[n], b[n])] is considered connected if every house number in the range
(min(a[1], a[2], ..., a[n]), max(b[1], b[2], ..., b[n])) is covered by at least one of the delivery zones (a[i], b[i]) in the set.

For an instance,

-  The set [(1, 2), (2, 3), (1, 5)] is connected because every house number in the interval (min(1, 2, 1), max(2, 3, 5)) = (1, 5)
is covered by at least one of the delivery zones.

-  The set [(2, 2), (3, 4)] is not connected because the delivery zones (2, 2) and (3, 4) do not overlap each other and hence is disconnected.

Note: The arrays 'a' and 'b' used above are considered to follow 1-based indexing.

Example

Consider the delivery zones:
[(1, 5), (2, 4), (6, 6), (7, 14), (16, 19)] and k = 2. If you add a new delivery zone (5, 7) to the list, you can separate the zones 
into 2 connected sets:

  o  [(1, 5), (2, 4), (5, 7), (6, 6), (7, 14)]
  o  [(16, 19)]


However, if you add a new delivery zone (14, 16), you will end up with 3 connected sets:

  o  [(1,5), (2, 4)]
  o  [(6,6)]
  o  [(7, 14), (14, 16), (16, 19)]

Therefore, the optimal solution is to add the delivery zone (5, 7), resulting in the minimum number of connected sets, which is 2.

#  Function Description

Complete the function minimumSets in the editor below.

minimumSets has the following parameter(s):
int a[n]: an integer array denoting the first parameters of intervals
int b[n]), an integer array denoting the second parameters of intervals
int k an integer denoting the maximum range of the delivery zone that can be added.

#  Returns
int: an integer denoting the minimum number of connected delivery zones after adding one delivery zone.

Sample Case:

Input: a=[1,2,5,10]; b=[2,4,8,11]; k = 2
Output : 2

Input: a=[3,2,3]; b=[5,9,3]; k=10
Output: 1

"""


def minmConnectedZones(a, b, k):
    n = len(a)
    if n == 0:
        return 1 # If no intervals exist, return 1 (you need at least one zone, even if artificial)

    segs = [(a[i], b[i]) for i in range(n)] # Create a list of tuples representing intervals.
    segs.sort() # sort the intervals by starting point to allow linear merging.

    merged = []
    merged.append(segs[0]) # merge the zones
    for i in range(1, n):
        L, R = segs[i]
        lastL, lastR = merged[-1]
        # If the next segment overlaps with or touches the last one, merge it.
        if L <= lastR:
            if R > lastR:
                merged[-1] = (lastL, R)
        else:
            merged.append((L, R))
    
    m = len(merged) # m: number of disconnected merged zones
    if m <= 1:
        return 1   # If only one zone remains, return 1.

    best = 0
    j = 0
    for i in range(m):
        if j < i:
            j = i
        # For each merged zone i, try to connect as many next zones as possible with one delivery zone of length ≤ k.
        while j + 1 < m and merged[j + 1][0] - merged[i][1] <= k:
            j += 1  
        merges = j - i  # how many zones we can connect from current i.
        if merges > best:  # Track the maximum number of merges we can do with one added segment of length ≤ k
            best = merges
    # If best merges were possible, we reduce the total number of zones by best.
    return m - best
    

if __name__ == "__main__":
    a=[1,2,5,10]
    b=[2,4,8,11]
    k = 2
    
    res = minmConnectedZones(a, b, k)
    print(f"The minimum number of connected delivery zones after adding one delivery zone: {res}")
    
    
    
