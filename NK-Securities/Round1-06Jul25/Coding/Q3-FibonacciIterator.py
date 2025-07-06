"""
# Q2.
Implement an iterable class named FibonaccuUterator that:
1. Accepts an integer parameter n in its constructor, representing the number of Fibonacci numbers to generate.
2. When iterated, yields the first n Fibonacci numbars in sequence.

The Fibonacci sequence starts with 0 and 1, and each subssequent number is the sum of the two preceeding numbers.

Example:
n = 4
Fibonacci = FibonacciIterator(4)

for num in fibonacci:
    print(num, end = " ")
    
The above code should output "0 1 1 2"

Function Description:
Complete the class FibonacciIterator in the editor with the following parameter:
int n: the number of fibonacci numbers to generate

Returns
Iterable: an iterable with the first n Fibonacci numbers.


Sample Case 0
Input:
5
Output:
0
1 
1 
2 
3
"""
class FibonacciIterator:
    def __init__(self, n):
        self.n = n
        self.count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.n:
            raise StopIteration
        if self.count == 0:
            self.count += 1
            return 0
        elif self.count == 1:
            self.count += 1
            return 1
        else:
            self.count += 1
            self.a, self.b = self.b, self.a + self.b
            return self.b

# Example usage:
fibonacci = FibonacciIterator(4)
for num in fibonacci:
    print(num, end=' ')  # Output: 0112
