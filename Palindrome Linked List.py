# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head is None: return True

        fast = head
        slow = head
        # find mid
        while fast.next and fast.next.next:
        	fast = fast.next.next
        	slow = slow.next
        #from mid, or next node after mid(if odd)
        p = slow.next
        temp = None
        while p:
        	next = p.next
        	p.next = temp
        	temp = p
        	p = next
        	# next.next = temp
        # compare
        start = head
        p1 = temp
        while p1 and start:
        	if p1.val == start.val:
        		p1 = p1.next
        		start = start.next
        	else : return False
        return True

