import collections
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        Counter = collections.Counter
        bull = 0
        cow = 0
        for i in range(len(secret)):
        	if secret[i] == guess[i]:
        		bull += 1
        cow = sum((Counter(secret) & Counter(guess)).values()) - bull
        return '%dA%dB' % (bull, cow)

if __name__=='__main__':
    asolution = Solution()
    print(asolution.getHint('1780', '8701'))