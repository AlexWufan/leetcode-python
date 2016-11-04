class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = []
        temp = temp2 = None
        count1, count2 = 0, 0
        for x in nums:
            if temp == x:
                count1 += 1
            elif temp2 == x:
                count2 += 1
            elif count1 == 0 :
                temp = x
                count1 = 1
            elif count2 == 0 :
                temp2 = x
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1
            # print(temp, count1, temp2, count2)

        for x in [temp, temp2]:
            if nums.count(x) > len(nums)/3:
                res.append(x)


        return res



if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.majorityElement([2,2]))