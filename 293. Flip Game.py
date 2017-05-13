class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                if s[i] == '+':
                    tmp = s[:i]+'--'+s[i+2:]
                    res.append(tmp)
        return res

if __name__ == '__main__':
    Asolution = Solution()
    print(Asolution.generatePossibleNextMoves('++++'))

# 一行
    def generatePossibleNextMoves(self, s):
    return [s[:i] + "--" + s[i + 2:] for i in xrange(len(s) - 1) if s[i:i + 2] == '++']