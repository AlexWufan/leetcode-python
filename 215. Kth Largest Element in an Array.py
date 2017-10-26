class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        q = []
        for num in nums:
            heapq.heappush(q,num)
        for i in range(len(nums)-k):
            heapq.heappop(q)
        return heapq.heappop(q)


class Solution:
# @param {integer[]} nums
# @param {integer} k
# @return {integer}
def findKthLargest(self, nums, k):
    # QuickSelect idea: AC in 52 ms
    # ---------------------------
    #
    pivot = nums[0]
    left  = [l for l in nums if l < pivot]
    equal = [e for e in nums if e == pivot]
    right = [r for r in nums if r > pivot]

    if k <= len(right):
        return self.findKthLargest(right, k)
    elif (k - len(right)) <= len(equal):
        return equal[0]
    else:
        return self.findKthLargest(left, k - len(right) - len(equal))

# inplace!!!!!!!!!!!!!!!!!!!!!!!!!
# O(n) time, quicksort-Partition method   
def findKthLargest(self, nums, k):
    pos = self.partition(nums, 0, len(nums)-1)
    if pos > len(nums) - k:
        return self.findKthLargest(nums[:pos], k-(len(nums)-pos))
    elif pos < len(nums) - k:
        return self.findKthLargest(nums[pos+1:], k)
    else:
        return nums[pos]
 
# Lomuto partition scheme   
def partition(self, nums, l, r):
    pivot = nums[r]
    lo = l 
    for i in xrange(l, r):
        if nums[i] < pivot:
            nums[i], nums[lo] = nums[lo], nums[i]
            lo += 1
    nums[lo], nums[r] = nums[r], nums[lo]
    return lo