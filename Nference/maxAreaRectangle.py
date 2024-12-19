"""
We have hiven an array of heights, H of size N. Find the maximum area of the rectangle of the histogram.

Examples:
Input:
N = 6, height = [2,1,5,6,2,3]
Output:
10
"""

def getMax_BruteForce(heights):
    n = len(heights)
    res = 0
    
    for i in range(n):
        curr = heights[i]
        j = i-1
        while j >= 0 and heights[j] >= heights[i]:
            curr += heights[i]
            j -= 1 
        
        j = i + 1 
        while j < n and heights[j] >= heights[i]:
            curr += heights[i]
            j += 1
        
        res = max(res, curr)
    return res

if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    res = getMax(heights)
    print(res)

def prevSmaller(heights):
    n = len(heights)
    prev = [-1]*n
    st = []
    for i in range(n):
        while st and heights[i] < heights[st[-1]]:
            st.pop()
        if st:
            prev[i] = st[-1]
        st.append(i)
    return prev
    
    

def nextSmaller(heights):
    n = len(heights)
    nextt = [n]*n
    st = []
    for i in range(n):
        while st and heights[i] < heights[st[-1]]:
            nextt[st.pop()] = i
        st.append(i)
    return nextt
    
    
    
def getMax(heights):
    n = len(heights)
    prevS = prevSmaller(heights)
    nextS = nextSmaller(heights)
    maxmArea = 0
    for i in range(n):
        width = nextS[i] - prevS[i] - 1
        area = width * heights[i]
        maxmArea = max(area, maxmArea)
    return maxmArea
        
        

if __name__ == "__main__":
    heights = [2,1,5,6,2,3]
    print("Brute Force approach to find maxm area of rectangle: ", getMax_BruteForce(heights))
    res = getMax(heights)
    print(res)
