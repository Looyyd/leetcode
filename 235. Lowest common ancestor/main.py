
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> TreeNode:
        # find p
        pstack = []

        node = root
        pstack.append(node)
        while node.val != p.val:
            if node.val > p.val:
                node = node.left
                pstack.append(node)
            else:
                node = node.right
                pstack.append(node)

        # find q
        qstack = []
        node = root
        qstack.append(node)
        while node.val != q.val:
            if node.val > q.val:
                node = node.left
                qstack.append(node)
            else:
                node = node.right
                qstack.append(node)

        # find common ancestor

        # make stacks same length
        while len(pstack) > len(qstack):
            pstack.pop()
        while len(qstack)> len(pstack):
            qstack.pop()

        while 1:
            p_pop = pstack.pop()
            q_pop = qstack.pop()
            if p_pop.val == q_pop.val:
                return p_pop
