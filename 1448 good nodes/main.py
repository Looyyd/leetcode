 #{Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        answer = 0
        queue = []
        if (root != None):
            queue.append((root,root.val))

        while (len(queue) != 0):
            node, max_val = queue.pop()
            if(node.val >= max_val):
                answer+=1
                max_val=node.val
            if(node.left!=None):
                queue.append((node.left, max_val))
            if(node.right!=None):
                queue.append((node.right,max_val))
        return answer



