class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        dict = {n:r for r,n in enumerate(sorted(nums,reverse = True))}
        medal = ["Gold Medal", "Silver Medal", "Bronze Medal"]
        res = [str(dict[num]+1) if dict[num]>2 else medal[dict[num]] for num in nums]
        return res