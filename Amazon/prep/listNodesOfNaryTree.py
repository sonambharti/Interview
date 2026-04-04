'''
Given a list of Nodes in a N-ary tree, and given a level you have to return the nodes at the level.

# Constructing a sample N-ary tree:
#        1
#      / | \
#     2  3  4
#        |
#        5


'''

from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children is not None else []

def nodes_at_level(root, target_level):
    if not root:
        return []
    
    queue = deque([root])
    current_level = 0
    
    while queue:
        level_size = len(queue)
        
        # If we reached the target level, return all node values in queue
        if current_level == target_level:
            return [node.val for node in queue]
        
        # Process current level
        for _ in range(level_size):
            node = queue.popleft()
            for child in node.children:
                queue.append(child)
        
        current_level += 1
    
    return []  # If level doesn't exist
    
    

if __name__ == "__main__":
    root = Node(1, [
        Node(2),
        Node(3, [Node(5)]),
        Node(4)
    ])
    
    print(nodes_at_level(root, 0))  # Output: [1]
    print(nodes_at_level(root, 1))  # Output: [2, 3, 4]
    print(nodes_at_level(root, 2))  # Output: [5]
        
