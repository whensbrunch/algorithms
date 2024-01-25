# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:       
        
        def inorder_iterator(node):
            if not node:
                return
            yield from inorder_iterator(node.left)
            yield node
            yield from inorder_iterator(node.right)
        
        for node in inorder_iterator(root):
            k -= 1
            if k == 0:
                return node.val
        
        return -1
