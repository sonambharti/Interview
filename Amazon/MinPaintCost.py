#Minimize the cost of painting N houses.
#Make sure 2 adjacent house is not painted in same color.

def minCost(costs, n):
    
    if n == 0:
        return 0
        
    #dp = [[0 for i in range(3)] for j in range(n)]
    #dp = [[0]*cols]*rows
    
    dp = [[0]*3]*n
    
    #Base Case
    dp[0][0] = costs[0][0]
    dp[0][1] = costs[0][1]
    dp[0][2] = costs[0][2]
    
    for i in range(1, n, 1):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + costs[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + costs[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + costs[i][2]
        
        
    return min(dp[n-1][0], min(dp[n-1][1], dp[n-1][1]))
    

if __name__ == '__main__':
    
    costs = [[1, 2, 3],
            [10, 11, 12]]
            
    n = len(costs)
    print(minCost(costs, n))
