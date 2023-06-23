# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _depth(node, n):
            if node == None:
                return n
            else:
                n+=1
                return max(_depth(node.left, n), _depth(node.right,n))

        return _depth(root, 0)