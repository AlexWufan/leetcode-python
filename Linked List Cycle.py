# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        a, b = head, head
        while a and a.next:
            a = a.next.next 
            b = b.next
            if a == b:
                return True
        return False