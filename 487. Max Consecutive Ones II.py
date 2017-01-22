class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not 0 in nums:
        	return len(nums)
        new = []
        tmp = 0
        for i in nums:
        	if i  == 1:
        		tmp += 1
        		if new == []:
        			new.append(tmp)
        		elif new[-1] == 0:
        			new.append(tmp)
        		else:
        			new[-1] = tmp
        	else:
        		tmp = 0
        		new.append(i)

        res = [1]*len(new)
        for i in range(len(new)):
        	if new[i] == 0:
        		if i-1>=0 :
        			res[i] += new[i-1]
        		if i+1<len(new):
        			res[i] += new[i+1]
        return max(res)

if __name__=='__main__':
    asolution = Solution()
    print(asolution.findMaxConsecutiveOnes([1,1]))