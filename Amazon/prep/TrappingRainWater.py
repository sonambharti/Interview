'''
# Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it can trap after raining.

 

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. 
In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''
class PrefixArray:
    def findLeftMax(self, n, height):
        left = []
        maxm = 0
        for i in range(0, n):
          maxm = max(maxm, height[i])
          left.append(maxm)
        return left
    
    
    def findRightMax(self, n, height):
        right = [-1] * n
        maxm = 0
        for i in range(n-1, -1, -1):
          maxm = max(maxm, height[i])
          right[i] = maxm
        return right
    
    
    def trap(self, height):
        n = len(height)
        ans = 0
        
        leftMax = self.findLeftMax(n, height)
        rightMax = self.findRightMax(n, height)
        
        for i in range(n):
          ans += min(leftMax[i], rightMax[i]) - height[i]
        return ans


class TwoPointers:
    def trap(self, height):
        n = len(height)
        leftMax = 0
        rightMax = 0
        
        start, end = 0, n-1
        ans = 0
        
        while start < end:
            leftMax = max(leftMax, height[start])
            rightMax = max(rightMax, height[end])
            
            if leftMax < rightMax:
                ans += leftMax - height[start]
                start += 1
                
            else:
                ans += rightMax - height[end]
                end -= 1
                
        return ans
            
        
if __name__ == "__main__":
    height = [4,2,0,3,2,5]
    print("Prefix array method: ", PrefixArray().trap(height))
    print("2 pointers method: ", TwoPointers().trap(height))

        
