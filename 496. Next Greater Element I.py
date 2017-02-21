class Solution(object):
    def nextGreaterElement(self, findNums, nums):
        """
        :type findNums: List[int]
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        dic = {value : index for index, value in enumerate(nums)}
        for n in findNums:
            for j in range(dic[n]+1,len(nums)):
                if nums[j] > n:
                    res.append(nums[j])
                    break
            if dic[n]+1 == len(nums) or j == len(nums)-1 and nums[j]<=n:
                res.append(-1)
        return res

#时间复杂度O(m*n)

#时间复杂度O(m+n)

	    stack = []
        dic = {}
        for n in nums:
            while stack and stack[-1] < n:
                # x = stack.pop()
                # dic[x] = n
                dic[stack.pop()] = n
            stack.append(n)
        return [dic.get(num, -1) for num in findNums]