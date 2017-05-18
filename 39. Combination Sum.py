class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, num, target, index, path, res):
        if target == 0:
            res.append(path)
            return None
        for i in range(index, len(num)):
            if num[i] > target:
                break
            self.dfs(num, target-num[i], i, path+[num[i]], res)