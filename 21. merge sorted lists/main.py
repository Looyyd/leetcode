# Definition for singly-linked list.
 class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        res = None

        curr = res

        while 1:
            if list1==None and list2==None:
                return res
            if list1==None:
                if res == None:
                    return list2
                else:
                    curr.next = list2
                    return res
            elif list2==None:
                if res == None:
                    return list1
                else:
                    curr.next = list1
                    return res
            elif list1.val > list2.val:
                if res == None:
                    res = ListNode(list2.val)
                    curr = res
                    list2=list2.next
                else:
                    curr.next = ListNode(list2.val)
                    curr=curr.next
                    list2=list2.next
            else:
                if res == None:
                    res = ListNode(list1.val)
                    curr = res
                    list1=list1.next
                else:
                    curr.next = ListNode(list1.val)
                    curr=curr.next
                    list1=list1.next


# better solution
class Solution2:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2

        if list1 or list2:
            cur.next = list1 if list1 else list2

        return dummy.next



