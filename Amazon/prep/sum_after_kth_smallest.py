'''
Find sum of n elements after kth smallest element in BST. Tree is very large, you are not allowed to
traverse the tree. Discussion : Since the array traversal is not allowed so we need to do some 
preprocessing over the tree, something like storing sum of all its predecessor nodes.For finding kth 
smallest element, use order statistics approach.
'''


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.size = 0  # Number of nodes in the left subtree

def update_size(node):
    if node:
        node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)

def insert(root, val):
    if not root:
        return TreeNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    update_size(root)
    return root

def find_kth_smallest(root, k):
    left_size = root.left.size if root.left else 0
    if k == left_size + 1:
        return root.val
    elif k <= left_size:
        return find_kth_smallest(root.left, k)
    else:
        return find_kth_smallest(root.right, k - left_size - 1)

def preprocess_tree(root):
    def inorder(node):
        if not node:
            return []
        return inorder(node.left) + [node.val] + inorder(node.right)
    
    sorted_elements = inorder(root)
    cumulative_sums = [0] * len(sorted_elements)
    cumulative_sums[0] = sorted_elements[0]
    for i in range(1, len(sorted_elements)):
        cumulative_sums[i] = cumulative_sums[i-1] + sorted_elements[i]
    return cumulative_sums

def sum_after_kth_smallest_optimized(cumulative_sums, k, n):
    if k > len(cumulative_sums) or k + n > len(cumulative_sums):
        return 0
    if k == 0:
        return cumulative_sums[k+n-1]
    return cumulative_sums[k+n-1] - cumulative_sums[k-1]

if __name__ == "__main__":
    # Example usage
    root = None
    values = [5, 3, 7, 2, 4, 6, 8]
    for value in values:
        root = insert(root, value)
    
    cumulative_sums = preprocess_tree(root)
    k = 3
    n = 3
    kth_smallest = find_kth_smallest(root, k)
    sum_result = sum_after_kth_smallest_optimized(cumulative_sums, k, n)
    print(sum_result)  # Output: 15 (6 + 8)
