# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p, q= l1, l2
        cur = ListNode(0)
        root = cur
        flag = 0
        while p or q or flag:
            node = ListNode(0)
            if p:
                node.val += p.val
                p = p.next
            if q:
                node.val += q.val
                q = q.next
            if flag:
                node.val += flag
                
            if node.val>9:
                node.val -= 10
                flag = 1
            else:
                flag = 0
            
            cur.next = node
            cur = cur.next
        return root.next
        
        