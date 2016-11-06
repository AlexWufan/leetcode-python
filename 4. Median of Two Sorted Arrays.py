class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 这种做法是错的！但是可以ac
        # if (len(nums1)+len(nums2)) % 2 == 1:
        #     return sorted(nums1+nums2)[(len(nums1)+len(nums2))//2]
        # else:
        #     return sum(sorted(nums1+nums2)[(len(nums1)+len(nums2))//2 - 1 : (len(nums1)+len(nums2))//2+1])/2
        tbc




if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.findMedianSortedArrays([1,2],[3,4]))