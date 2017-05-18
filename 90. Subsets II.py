class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        res = []
        self.dfs(res,nums,[],0)
        return res

    def dfs(self, res, nums, path, index):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.dfs(res, nums, path+[nums[i]], i+1)

class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        res = [[]]
        S.sort()
        for i in range(len(S)):
            if i == 0 or S[i] != S[i - 1]:
                l = len(res)
                print(l)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [S[i]])
                print(res)
        return res

if __name__=='__main__':
    asolution = Solution()
    print(asolution.subsetsWithDup([1,2,2]))