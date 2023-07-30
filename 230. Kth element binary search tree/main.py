from typing import List, Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        stack:TreeNode = []

        def add_left_to_stack(node:TreeNode):
            while node != None:
                stack.append(node)
                node=node.left

        current_node = root
        add_left_to_stack(current_node)
        while 1:
            # pop
            k -= 1
            poped_node = stack.pop()
            if k == 0:
                return poped_node.val
            if poped_node.right != None:
                add_left_to_stack(poped_node.right)


