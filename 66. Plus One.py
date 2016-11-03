# class Solution(object):

#     def plusOne(self, digits):
#         """
#         :type digits: List[int]
#         :rtype: List[int]
#         """
#         string = ''
#         for x in digits:
#         	string += str(x)
#         return [int(x) for x in list(str(int(string)+1))]
from functools import reduce
class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        v = 0
        for i in range(len(digits)):
        	# v += digits[len(digits)-i-1]*10**i
        	# 更好的写法
        	v = v * 10 + digits[i] 
        # 使用reduce
        v = reduce(lambda x,y: x*10+y, digits)
        return list(int(x) for x in str(v+1))



if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.plusOne([1,2,3,9]))


# 第一种写法不好，因为如果数字大于2^32无效了
# 更好的写法是第二种
