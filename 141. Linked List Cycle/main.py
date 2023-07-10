from typing import Optional
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        cur = head

        passedNodes = {}
        while cur != None:
            if cur in passedNodes.keys():
                return True
            else:
                passedNodes[cur] = True
                cur = cur.next


        # reached None so no cycle
        return False
