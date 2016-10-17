# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = head
        while a and a.next:
        	if a.val == a.next.val:
        		a.next = a.next.next
        	else :
        		a = a.next
        return head