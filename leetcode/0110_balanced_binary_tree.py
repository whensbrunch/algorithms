
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def __init__(self):
        self.cache = {}

    def isBalanced(self, root: TreeNode | None) -> bool:
        if not root: 
            return True

        def depth(root: TreeNode | None):
            if not root:
                return 0
            if root in self.cache:
                return self.cache[root]
            l = depth(root.left)
            r = depth(root.right)
            self.cache[root] = 1 + max(l, r)
            return self.cache[root]
        return (
             abs(depth(root.left) - depth(root.right)) <= 1
             and self.isBalanced(root.left)
             and self.isBalanced (root.right)
        )
    
    
        