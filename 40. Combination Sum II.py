class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target == 0:
            res.append(path)
            return None
        for i in range(index, len(nums)):
            if nums[i] > target: #pruning
                break
            if i > index and nums[i] == nums[i-1]: # avoid duplicates，横向的
                continue
            self.dfs(nums, target-nums[i], i+1, path+[nums[i]], res)
