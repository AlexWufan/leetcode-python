class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        if num < 0: num = (-num ^ 0xffffffff) + 1 #equals  if num < 0: num = num + 2**32
        res = ''
        dict = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        while(num):
            res = dict[num&15] + res
            num = num >> 4
        return res