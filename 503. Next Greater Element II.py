class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = []
        res = [-1 for i in nums]
        for i in range(2*len(nums)):
            j = i%len(nums)
            n = nums[j]
            while stack and nums[stack[-1]] < n:
                x = stack.pop()
                res[x] = n
            if i < len(nums):
                stack.append(i)
        return res
# 上面的解法要好很多
# 下面的解法空间更多

        stack = []
        dic = {}
        for i in range(2*len(nums)):
            j = i%len(nums)
            n = nums[j]
            while stack and stack[-1][1] < n:
                # x is a tuple,like(index,number)
                x = stack.pop()
                dic[x] = n
            if i < len(nums):
                stack.append((i,n))
        return [dic.get((i,nums[i]),-1) for i in range(len(nums))]


if __name__=='__main__':
    asolution = Solution()
    print(asolution.nextGreaterElements([1,2,1]))