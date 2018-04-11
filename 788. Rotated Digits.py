class Solution(object):
    def rotatedDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        count = 0
        for x in range(1,N+1):
            s = str(x)
            if '3' in s or '4' in s or '7' in s:
                continue
            elif '2' in s or '5' in s or '6' in s or '9' in s:
                count+=1
        return count