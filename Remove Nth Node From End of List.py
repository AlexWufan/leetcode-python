# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        p1=p2=p3 = ListNode(0)
        p1.next = head
        p2.next = head
        p3.next = head
        for i in range(n): p1 = p1.next
        while p1.next :
        	p1 = p1.next
        	p2 = p2.next
        p2.next = p2.next.next
        return p3.next


if __name__=='__main__':
    asolution = Solution()
    print(asolution.removeNthFromEnd()