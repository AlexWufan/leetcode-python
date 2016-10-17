# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        a = headA
        b = headB
        while a != b:
        	a = a.next if a else headB
        	b = b.next if b else headA
        gc.collect()
        return a

import gc

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        a, b = headA, headB
        while a is not b:
            a = headB if a is None else a.next
            b = headA if b is None else b.next
        
        # clean the memory
        gc.collect()
        return a

# 解法2
        # if headA is None or headB is None:
        #     return None

        # pa = headA # 2 pointers
        # pb = headB

        # while pa is not pb:
        #     # if either pointer hits the end, switch head and continue the second traversal, 
        #     # if not hit the end, just move on to next
        #     pa = headB if pa is None else pa.next
        #     pb = headA if pb is None else pb.next

        # return pa



# 解法1

  #       a, b = headA, headB
		# while a != b:
  #   		a = a.next if a else headB
  #   		b = b.next if b else headA
		# return a
