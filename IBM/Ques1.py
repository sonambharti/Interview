"""
There are n types of items in a shop, where the number of items of type i is denoted by quantity[I]. 
The price of the items is determined dynamically, where the price of the 5th item is equal to the 
remaining number of items of type i. There are m customers in line to buy the items from the shop, 
and each customer will buy exactly one item of any type.

The shopkeeper being greedy, tries to sell the items in a way that maximises revenue. Find the 
maximum amount shopkeeper can earn by selling exactly m items to the customers optimally.

Example:
Input: n = 3, m = 4, quantity = [1,2,4]
Output: 11
"""

import heapq

def maxRevenue(n, m, quantity):
    # Step 1: Convert quantity into a max-heap (using negative values)
    max_heap = [-q for q in quantity]
    heapq.heapify(max_heap)
    
    revenue = 0
    
    # Step 2: Process each customer
    for _ in range(m):
        # Get the item with the maximum quantity
        max_qty = -heapq.heappop(max_heap)  # Convert back to positive
        
        # Add to revenue
        revenue += max_qty
        
        # If there are more items left of this type, push the reduced quantity back
        if max_qty - 1 > 0:
            heapq.heappush(max_heap, -(max_qty - 1))
    
    return revenue

# Example usage:
if __name__ == "__main__":
    n = 3
    m = 4
    quantity = [1, 2, 4]
    print(maxRevenue(n, m, quantity))  # Output: 11


# Time Complexity: O(m log n)
# Space Complexity: O(n)

"""
Since we want to maximize revenue, the shopkeeper should always sell the item with the highest quantity 
available because its price will be the highest at that point. After selling one item of that type, the 
price of the next item will decrease by 1. Therefore, our approach should always pick the item with the
highest quantity left.
"""
