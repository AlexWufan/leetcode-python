# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(0)
        dummy.next = head
        a = head
        dummy2 = ListNode(-1)
        tail = dummy2
        pre = dummy

        while a and a.next:
            tail.next = a.next
        	tail = tail.next
        	pre.next = a
        	a.next = a.next.next
        	pre = a 
        	a = a.next
        if a :
            pre.next = a
            tail.next = None
            a.next = dummy2.next
        else :
        	pre.next = dummy2.next
        return head

# 解法2 更好

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None: return head
        odd = head
        evenstart = head.next
        while odd.next is not None and odd.next.next is not None:
        	even = odd.next
        	odd.next = even.next
        	odd = odd.next
        	even.next = odd.next
        odd.next = evenstart
        return head
