# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def _isBalanced(node):
            if node == None:
                return True,0 # isBalanced, depth
            else:
                balancedRight, depthRight = _isBalanced(node.right)
                balancedLeft, depthLeft = _isBalanced(node.left)
                if not balancedRight or not balancedLeft:
                    return False, max(depthRight,depthLeft) + 1 # depth doesn't matter if not balanced
                else:
                    if abs(depthRight-depthLeft)<= 1:
                        return True, max(depthRight,depthLeft) + 1
                    else:
                        return False, max(depthRight,depthLeft) + 1

        rootBalanced, _ = _isBalanced(root)
        return rootBalanced

