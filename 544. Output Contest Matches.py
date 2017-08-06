class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        nums = [i for i in range(1,n+1)]
        k = int(math.log(n,2))
        for i in range(k):
            pair = self.helper(nums)
            nums = pair
        return str(nums[0]).replace(' ','')
    
    def helper(self,nums):
        pair = list(zip(nums,nums[::-1]))[:len(nums)/2]
        return pair

class Solution(object):
    def findContestMatch(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = [str(i) for i in range(1,n+1)]
        while n>1:
            for i in range(n/2):
                res[i] = '(' + res[i] + ','+ res[n-1-i] + ')'
            n = n/2
        return res[0]