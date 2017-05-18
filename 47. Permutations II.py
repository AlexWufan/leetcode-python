class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        used = [False for _ in nums]
        self.dfs(res, nums, [], used)
        return res

    def dfs(self, res, nums, path, used):
        if len(path) == len(nums):
            res.append(path)
            return
        for i in range(len(nums)):
            if used[i] or i > 0 and nums[i] == nums[i-1] and used[i-1] == False:
                continue
            used[i] = True
            self.dfs(res, nums, path+[nums[i]], used)
            used[i] = False




def permuteUnique(self, nums):
    ans = [[]]
    for n in nums:
        new_ans = []
        for l in ans:
            for i in xrange(len(l)+1):
                new_ans.append(l[:i]+[n]+l[i:])
                if i<len(l) and l[i]==n: break              #handles duplication
        ans = new_ans
    return ans