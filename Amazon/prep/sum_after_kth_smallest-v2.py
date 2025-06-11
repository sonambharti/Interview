'''
Find sum of n elements after kth smallest element in BST. Tree is very large, you are not allowed to
traverse the tree. Discussion : Since the array traversal is not allowed so we need to do some 
preprocessing over the tree, something like storing sum of all its predecessor nodes.For finding kth 
smallest element, use order statistics approach.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = self.right = None
        self.left_count = 0
        self.subtree_sum = val

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def BruteForce(root, k, n):
    def inorder(root, arr):
        if not root:
            return
        inorder(root.left, arr)
        arr.append(root.val)
        inorder(root.right, arr)
    
    def sum_after_kth_smallest(root, k, n):
        arr = []
        inorder(root, arr)
        if k >= len(arr):
            return 0
        return sum(arr[k:k+n])
    
    return sum_after_kth_smallest(root, k, n)
    
def Optimum(root, k, n):
    # Augment the tree with left_count and subtree_sum
    def preprocess(node):
        if not node:
            return 0, 0
        left_nodes, left_sum = preprocess(node.left)
        right_nodes, right_sum = preprocess(node.right)
        
        node.left_count = left_nodes
        node.subtree_sum = left_sum + right_sum + node.val
        
        return left_nodes + right_nodes + 1, node.subtree_sum
    
    # Order-statistics to find kth smallest
    def find_kth_smallest(node, k):
        while node:
            if node.left_count + 1 == k:
                return node
            elif k <= node.left_count:
                node = node.left
            else:
                k -= (node.left_count + 1)
                node = node.right
        return None
    
    # Inorder successor helper
    def inorder_successor(root, node):
        succ = None
        while root:
            if node.val < root.val:
                succ = root
                root = root.left
            else:
                root = root.right
        return succ
    
    # Sum next n elements starting from given node
    def sum_next_n(root, node, n):
        stack = []
        curr = node
        # Find the first element greater than node (inorder successor)
        found = False
        result = 0
    
        def push_left_path(start):
            while start:
                stack.append(start)
                start = start.left
        push_left_path(root)
        while stack and n > 0:
            curr = stack.pop()
            if found:
                result += curr.val
                n -= 1
            if curr == node:
                found = True
            push_left_path(curr.right)
    
        return result
    
    # Main function
    def sum_after_kth_smallest(root, k, n):
        preprocess(root)
        kth_node = find_kth_smallest(root, k)
        if not kth_node:
            return 0
        return sum_next_n(root, kth_node, n)
        
    return sum_after_kth_smallest(root, k, n)

if __name__ == "__main__":
    # Example usage
    root = None
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        root = insert(root, value)
    k = 3
    n = 2
    
    print("BruteForce: ", BruteForce(root, k, n))
    print("Optimum: ", Optimum(root, k, n))
    
    
