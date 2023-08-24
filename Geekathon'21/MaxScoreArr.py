"""
Given an array "arr" of positive integers with length N, your goal is to achieve the maximum possible score by removing elements from either the beginning or the end of the array. The score for removing an element is calculated as:

Score = element * length(arr) + minimum(arr)

Here, "arr" is considered before the current operation, and you can choose to remove elements from the start or end of the array.
"element" represents the value of the removed element. 

Example:
N = 2
arr = {1, 2}
Output: 7
"""
def helper(i, j, arr, arr_min, dp):

  # DP - memoization approach 
  if (i == j):
      return arr[i] + arr_min[i][j]
      
  if (dp[i][j] != -1):
      return dp[i][j]
      
  
  left_score = arr[i] * (j - i + 1) + arr_min[i][j] + helper(i + 1, j, arr, arr_min, dp) 
  right_score = arr[j] * (j - i + 1) + arr_min[i][j] + helper(i, j - 1, arr, arr_min, dp)
  
  dp[i][j] = max(left_score, right_score)
  
  return dp[i][j]

      
def MaxScore(self, N, arr):
  # code here
  
  arr_min = [[0]*N]*N
  dp = [[-1]*N]*N
  
  for i in range(0, N):
      minm = 1e9+7
      for j in range(i, N):
          minm = min(minm, arr[j])
          arr_min[i][j] = minm
            
  return helper(0, N-1, arr, arr_min, dp)

  
if __name__ == '__main__':
  arr = [2, 3, 4]
  n = len(arr)
  
  res = MaxScore(n, arr)
  print(res)
