# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head: return None

        pre, slow, fast =None, head, head

        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next

        print slow.val
        root = TreeNode(slow.val)
        pre.next = None

        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        slow.next = None

        return root
# 时间复杂度O(nlgn)

# 下面的时间复杂度O(n)，bottom-up
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        # if not head: return None
        size = 0
        p = head
        while p:
            size += 1
            p = p.next
        self.node = head
        return self.inorderhelper(0, size-1)
        
    def inorderhelper(self, start, end):
        if start > end:
            return None
        mid = (start+end) >> 1
        l = self.inorderhelper(start, mid-1)
        root = TreeNode(self.node.val)
        root.left = l
        self.node = self.node.next
        root.right = self.inorderhelper(mid+1, end)
        return root
		
			
			
			

