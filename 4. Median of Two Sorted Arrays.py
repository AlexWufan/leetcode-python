class Solution(object):
    def findMedianSortedArrays(self, A, B):
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

        # 敲一遍别人的代码
        l = len(A)+len(B)
        return self.findKth(A,B,l//2) if l%2==1 else (self.findKth(A,B,l//2-1)+self.findKth(A,B,l//2))/2.0

    def findKth(self,A,B,k):
    	if len(A)>len(B):
    		A,B = B,A
    	if not A:
    		return B[k]
    	if k==len(A)+len(B)-1:
    		return max(A[-1],B[-1])
    	i = min(len(A)-1, k/2)
        j = min(len(B)-1, k-i)
    	if A[i]>B[j]:
    		return self.findKth(A[:i],B[j:],i)
    	else:
    		return self.findKth(A[i:],B[:j],j)






if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.findMedianSortedArrays([1,2],[3,4]))