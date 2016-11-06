class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 1, len(nums)
        while l<r:
        	mid = (l+r)//2
        	count = sum(1 for x in nums if x <= mid)
        	print (l,r,mid,count)

        	if count <= mid:
        		l = mid+1
        	else:
        		r = mid
        return l



if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.findDuplicate([1,2,3,4,5,5,6,7]))


# 快慢指针，时间复杂度O(nlgn) 代码来自http://bookshadow.com/weblog/2015/09/28/leetcode-find-duplicate-number/
class Solution(object):
    def findDuplicate(self, nums):
        # The "tortoise and hare" step.  We start at the end of the array and try
        # to find an intersection point in the cycle.
        slow = 0
        fast = 0
    
        # Keep advancing 'slow' by one step and 'fast' by two steps until they
        # meet inside the loop.
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
    
            if slow == fast:
                break
    
        # Start up another pointer from the end of the array and march it forward
        # until it hits the pointer inside the array.
        finder = 0
        while True:
            slow   = nums[slow]
            finder = nums[finder]
    
            # If the two hit, the intersection index is the duplicate element.
            if slow == finder:
                return slow