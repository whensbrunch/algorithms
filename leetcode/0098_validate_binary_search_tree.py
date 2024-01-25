# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:

        def inorder_traversal(node):
            if not node:
                return
            yield from inorder_traversal(node.left)
            yield node.val
            yield from inorder_traversal(node.right)
        
        prev_val = float('-inf')
        for curr_val in inorder_traversal(root):
            if prev_val >= curr_val:
                return False
            prev_val = curr_val
        
        return True