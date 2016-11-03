import collections
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for x in nums:
        	if count == 0:
        		temp = x
        		count = 1
        	elif x == temp:
        		count += 1
        	else:
        		count -= 1
        return temp



if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.majorityElement([1,2,3,4,1,1,1,1,1]))




# 不太好的方法，linear time，但是需要空间
# return collections.Counter(nums).most_common(1)[0][0]

# 摩尔投票 moore voting algorithm， 进出栈 只需要o(1)空间

# 还有一种 排序后中间那个，时间复杂度 nlogn