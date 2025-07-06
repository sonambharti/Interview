"""
Question 12

Implement a square operation on an input array of any The operation should

1. Aduly only to imagens greater than going off cars
2. Square each positivre integer.
3. Return a new array containing only the squared positive integers.

The input is not a regular 2D array, as rows can have differers rumbers of elements.

Example
arr = [[-1,1,2,-2,6],[3,4,-5]]

First remove elements <= 0: arr' = [[1,2,6],[3,4]]. THen find their square each element: res = [[1,4,36], [9,16]],



"""
def lambdaMap(arr):
    return [[x * x for x in sub if x > 0] for sub in arr]
    
arr = [[-1,1,2,-2,6],[3,4,-5]]
res = lambdaMap(arr)
print(res)
