Swap Nodes in Pairs# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        a = head
        pre = dummy
        while a and a.next:
            b = a.next
            pre.next, a.next, b.next, pre = b, a.next.next, a, a
            a = a.next
        return dummy.next