"""
The students of Hackerland love math problems.
the teacher decided to test their mathematical 
abilities and asked them to find the number of positive integers
less than or equal to k for a given integer k such that the sum 
of their digits is divisible by the integer m.

The students are stuck and need your help to get to the answer.
"""

def countIntegers(k, m):
  count = 0
  for i in range(1, k+1:):
    sum = 0
    while i>0:
      rem = i%10
      sum += rem
      i = i//10
    if sum%m == 0:
      count += 1
  return count%(10**9 + 7)

if __name__ == '__main__':
  k = int(input())
  m = int(input())
  res = countIntegers(k, m)
  print(res)
      
                  
