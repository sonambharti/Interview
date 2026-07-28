def getMinTime(n, cache):
    cnt = [0] * n

    for service in cache:
        cnt[service - 1] += 1

    def feasible(T):
        overflow = 0
        extra = 0

        for c in cnt:
            if c > T:
                overflow += c - T
            else:
                extra += (T - c) // 2

        return extra >= overflow

    left, right = 0, 2 * len(cache)

    while left < right:
        mid = (left + right) // 2
        if feasible(mid):
            right = mid
        else:
            left = mid + 1

    return left


# ---------------- Driver Code ----------------
if __name__ == "__main__":
    tests = [
        # Sample Case 0
        (4, [1, 2, 3, 4], 1),
    
        # Sample Case 1
        (4, [3, 3, 1, 4, 2, 1], 2),
    
        # Example from problem statement
        (3, [2, 1, 3, 1, 1], 3),
    
        # All requests cached in one service
        (3, [1, 1, 1], 2),
    
        # Single service
        (1, [1, 1, 1, 1], 4),
    
        # Balanced requests
        (2, [1, 2, 1, 2], 2),
    
        # Larger imbalance
        (5, [1, 1, 1, 1, 2, 3, 4], 3),
    ]
    
    for i, (n, cache, expected) in enumerate(tests, 1):
        ans = getMinTime(n, cache)
        status = "PASS" if ans == expected else "FAIL"
        print(f"Test {i}: {status}")
        print(f"n = {n}")
        print(f"cache = {cache}")
        print(f"Expected = {expected}, Got = {ans}\n")
