"""
Find the longest alternating substring after at most one flip.

Examples:
Sample Example 1:
s = "11101"
Output: 5

Sample Example 2:
s = "1111101"
Output: 5

Sample Example 3:
s = ""
Output: 0

"""

def solveBinaryString(s):
    n = len(s)
    if n == 0:
        return 0

    left = [1] * n          # longest alternating run ending at i
    for i in range(1, n):
        left[i] = left[i - 1] + 1 if s[i] != s[i - 1] else 1

    right = [1] * n         # longest alternating run starting at i
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] + 1 if s[i] != s[i + 1] else 1

    ans = max(left)         # no flip

    for i in range(n):
        cur = 1
        if i > 0 and s[i - 1] == s[i]:      # flipped char now differs from s[i-1]
            cur += left[i - 1]
        if i < n - 1 and s[i + 1] == s[i]:  # flipped char now differs from s[i+1]
            cur += right[i + 1]
        if cur > ans:
            ans = cur

    return ans

if __name__ == "__main__":
    s = "11101"
    res = solveBinaryString(s)
    print(f"Longest Possible alternate string: {res}")
