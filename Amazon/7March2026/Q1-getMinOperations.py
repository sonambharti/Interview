"""
Imagine you're managing an Amazon warehouse with two arrays: stockLevel and operation. The array stockLevels represents the 
stock levels of m products, and the array operations of size n represents operations that can be performed.

During the i-th operation, you can perform one of the following actions:

Decrement the stock of any product in stockLevel by at most 7 (to simulate fulfilling orders or reducing inventory). 
If operation[i]> 0 and stockdeveloperation[ill Q, the product at index operationil of stockLevel can be marked as out of 
stock frepresented as NU). Note that here, /< 1+ len(operation).

Assume indexing starts from 1. Your task is to determine the minimum number of operations required to mark all the products 
in stockLevel as NULL. If it is not possible to mark all products as NULL, return-2

Example:

Consider n= 4 and m = 2

operation = [0, 1, 0, 21], stockLevel[] = [1, 1]

1. In the first operation, decrement the stock of product L The stockLevel becomes (0, 11)
2. In the second operation, since operation[2]=1 and stockLevel 0, product 1 can be marked as NULL. The stockLevel becomes [NULL, 1]
3. In the third operation, decrement the stock of product 2. The stockLevel becomes [NULL, 0].
4. In the fourth operation, since operation[4] = 2 and stockLevel[2] = 0, product 2 can be marked as NULL. The stockLevel becomes [NULL, NULL]

This is one  optimal path. The minimum number of operations is 4.

"""
def getMinOperations(operation, stockLevel):
    n = len(operation)
    m = len(stockLevel)
    
    last = [-1] * m  
    
    for i, op in enumerate(operation):  
        if op > 0 and op <= m:  
            last[op - 1] = i  
    
    for i in range(m):  
        if last[i] == -1:  
            return -1  
    
    tasks = [(last[i], stockLevel[i]) for i in range(m)]  
    tasks.sort()  
    
    used = 0  
    
    for deadline, stock in tasks:  
        # operations available before deadline  
        available = deadline - used  
    
        if available < stock:  
            return -1  
    
        used += stock + 1  # decrements + mark  
    
    return used



if __name__ == "__main__":
  operation = [1, 0, 1, 3, 2, 1, 0, 3, 1, 1]
  stockLevel = [2, 1, 2]
  print(f"Minimum no. of operations: {getMinOperations(operation, stockLevel)}")
  
