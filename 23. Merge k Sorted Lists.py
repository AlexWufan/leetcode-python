# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode(None)
        head = dummy
        q = []
        for node in lists:
            if node:
                heapq.heappush(q,(node.val,node))
        while q:
            node = heapq.heappop(q)[1]
            head.next = node
            head = node
            if node.next:
                heapq.heappush(q,(node.next.val,node.next))
        return dummy.next