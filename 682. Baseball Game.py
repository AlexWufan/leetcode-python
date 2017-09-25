class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        res = []
        for x in ops:
            if x == '+':
                res.append(res[-1]+res[-2])
            elif x == 'D':
                res.append(res[-1]*2)
            elif x == 'C':
                res.pop()
            else:
                res.append(int(x))
        return sum(res)