# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def _max_diameter(node):
            if node == None:
                return 0, 0 # depth/max_diameter
            else:
                depth_l, diamater_l = _max_diameter(node.left)
                depth_r, diameter_r = _max_diameter(node.right)
                max_depth = max(depth_r, depth_l) + 1
                max_diameter = max(depth_r+depth_l, diameter_r, diamater_l)
                return max_depth,max_diameter

        _ , max_diameter = _max_diameter(root)
        return max_diameter
