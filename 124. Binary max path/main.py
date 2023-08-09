from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        max_path = -10000 # min number is -1000

        def _maxPathSum(node: Optional[TreeNode]) -> int:
            nonlocal max_path
            if node == None:
                return 0
            else:
                largest_left = _maxPathSum(node.left)
                largest_right = _maxPathSum(node.right)
                max_path = max(largest_right + node.val, largest_left + node.val, largest_left+largest_right + node.val, node.val, max_path)
                return max(largest_right + node.val, largest_left + node.val, node.val)

        _maxPathSum(root)

        return max_path