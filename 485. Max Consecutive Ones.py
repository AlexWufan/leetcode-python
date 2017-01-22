class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        length = 0
        for i in nums:
        	if i == 1:
        		length += 1
        	else:
        		length = 0
        	if length>res:
        		res = length
        return res

if __name__=='__main__':
    asolution = Solution()
    print(asolution.findMaxConsecutiveOnes([1,0]))
