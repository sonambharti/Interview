'''
# Unique paths in a Grid with Obstacles

A forklift operator navigates products within an automotive parts warehouse. 
The dashboard displays a real-time map showing open and blocked sections as
an n x m matrix of 1's (open) and O's (blocked). The operator starts at the 
top-left corner of the map at warehouse[0][0] and aims to reach the bottom-right
corner at warehouse[n-1] [m-1]. Movements can only be made to the right or downward. 
Given the warehouse map, calculate the number of distinct paths from warehouse[0][0] 
to warehouse[n-1][m-1]. Return the result modulo (10**9+7).


Example

warehouse = [[1, 1, 0, 1], [1, 1, 1, 1]]

The matrix below is drawn from the warehouse array showing open and blocked sections of
the warehouse. 1 indicates an open section and O indicates a blocked section. It is only
possible to travel through open sections, so no path can go through the section at (0, 2).

There are 2 possible paths from warehouse[0][0] to warehouse[1][3] and
2 modulo (10**9 + 7).

Returns
int: the number of paths through the matrix, modulo (10**9 + 7).


Sample Input 0:
n = 3, m = 4
warehouse = [[1,1,1,1], [1,1,1,1], [1,1,1,1]]

Sample Output 0:
10

Sample Input 1:
n = 2, m = 2
warehouse = [[1,1], [0,1]]

Sample Output 1:
1
'''

def numPaths(warehouse):
    n = len(warehouse)
    m = len(warehouse[0]) if n > 0 else 0  # Ensure m is correctly determined
    MOD = 10**9 + 7

    if n == 0 or m == 0 or warehouse[0][0] == 0 or warehouse[n-1][m-1] == 0:
        return 0  # No valid paths if start or end is blocked

    dp = [[0] * m for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if warehouse[i][j] == 0:  # Blocked cell
                dp[i][j] = 0
                continue

            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j - 1]  # First row, only from left
            elif j == 0:
                dp[i][j] = dp[i - 1][j]  # First column, only from top
            else:
                dp[i][j] = (dp[i - 1][j] + dp[i][j - 1]) % MOD  # Paths from top and left

    return dp[n - 1][m - 1]


if __name__ == "__main__":
    # Example usage
    n = int(input())
    m = int(input())
    warehouse = [input().strip() for _ in range(n)]
    # warehouse = [[1,1,1,1], [1,1,1,1], [1,1,1,1]]
    # warehouse = [[1,1], [0,1]]
    
    # Calculate and print the result
    result = numPaths(warehouse)
    print(result)
