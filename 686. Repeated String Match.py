class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        times = int(math.ceil(float(len(B))/len(A)))
        if B in A*times:
            return times
        elif B in A*(times+1):
            return times+1
        else:
            return -1
            