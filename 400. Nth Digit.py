class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        lenth = 0
        count = 0
        while n > count:
            count += 10**lenth * 9 * (lenth+1)
            lenth += 1
            
        pre = count - 10**(lenth-1) * 9 *lenth
        number = (n-1-pre)//lenth + 10**(lenth-1)
        print(number)
        return int(str(number)[(n-pre) % lenth -1])
        