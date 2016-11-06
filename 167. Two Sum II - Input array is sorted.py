class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictionary#############
        dic = {}
        for i in range(len(numbers)):
        	if target-numbers[i] in dic:
        		return [dic[target-numbers[i]]+1, i+1]
        	else:
        		dic[numbers[i]] = i 
        

        # two pointer #############
        # l = 0
        # r = len(numbers)-1
        # while l<r:
        # 	if numbers[l]+numbers[r] == target:
        # 		return [l+1, r+1]
        # 	elif numbers[l]+numbers[r] > target:
        # 		r -= 1
        # 	else:
        # 		l += 1


        

if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.twoSum([2,7,11,15],9))

