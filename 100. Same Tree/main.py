from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def recursiveIsSameTree(p: Optional[TreeNode], q: Optional[TreeNode]):
            if p == None and q == None:
                return True
            elif p ==None or q ==None:
                return False
            else:
                if p.val != q.val:
                    return False
                else:
                    left = recursiveIsSameTree(p.left, q.left)
                    right = recursiveIsSameTree(p.right, q.right)
                    return left and right

        return recursiveIsSameTree(p,q)
