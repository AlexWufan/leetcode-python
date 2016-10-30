class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(list(set(nums)))[-3] if len(set(nums))>=3 else max(nums)

if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.thirdMax([2, 1]))



# 上面写的是错误的 set（）用o（n）时间，sorted nlgn, 但是由于测试问题反而更快
#
# 用堆排序
import heapq
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        heapq.nlargest(3, set(nums))[2 if len(set(nums))>2 else 0]

这个地方，是过不了的，heapq 在中间步骤中会把2排到1前面，heap并不是按照顺序排的！

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = [float('inf')] * 3
        for n in nums:
        	if n not in l and n > l[0] :
        		heapq.heappushpop(l, n)
        		print(l)
        return l[0] if l[0]> float('-inf') else l[-1]


def thirdMax(nums):
    l = [float('-inf')] * 3
    for n in nums: l[0] < n not in l and heapq.heappushpop(l, n)
    return l[0] if l[0] > float('-inf') else max(l)



# 不用堆的写法，连续两次删掉max
def thirdMax(self, nums):
        nums = list(set(nums))
        if len(nums) < 3:
            return max(nums)
        nums.remove(max(nums))
        nums.remove(max(nums))
        return max(nums)