class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        res = []
        self.dfs(res,nums,target,[])
        return len(res)
    
    def dfs(self, res, nums, target, path):
        if target < 0: return None
        elif target == 0:
            res.append(path)
            return None
        else:
            for i in nums:
                if i > target:
                    break
                self.dfs(res, nums, target-i, path+[i])
#!!!!!!!!!!!!!!!! MLE !!!!!!!!!!!!

#!!!!!!!!!!!!!!!! DP!!!!!!!!!!!!!
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dp = [1] + [0]*(target)
        for i in range(target+1):
            for num in nums:
                if num > i: break
                elif num == i: dp[i]+=1
                else: dp[i] += dp[i-num]
        return dp[target]