class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        res = []
        for i in range(left, right+1):
            digits = str(i)
            if '0' not in digits and all(i % int(digit) == 0 for digit in digits):
                res.append(i)
        return res