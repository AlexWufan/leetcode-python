class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if abs(x) > 0x7fffffff or int(str(abs(x))[::-1]) > 0x7fffffff:
        	return 0

        if x >= 0:
        	return int(str(x)[::-1])

        if x < 0:
        	return -int(str(-x)[::-1])

if __name__=='__main__':
    asolution = Solution()
    print(asolution.reverse(1534236469))

# better way 




def reverse(num):
  rev = 0
  while num > 0:
    rev = (10*rev) + num%10
    num //= 10
  return rev
# class Solution(object):
#     def reverse(self, x):
#         """
#         :type x: int
#         :rtype: int
#         """
#         sign = -1 if x < 0 else 1
#         result = int(str(abs(x))[::-1])
#         if result > 0x7fffffff:
#             return 0
#         else:
#             return result *sign