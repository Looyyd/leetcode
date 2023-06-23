# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        dummy = curr = ListNode()
        reminder = 0
        while l1 or l2 or reminder>0:
            if l1 == None:
                l1=ListNode(0)
            if l2 == None:
                l2 = ListNode(0)
            n = l1.val + l2.val + reminder
            modulo = n%10
            curr.next = ListNode(modulo)
            curr=curr.next
            reminder = n // 10

            l1 = l1.next
            l2 = l2.next

        return dummy.next



