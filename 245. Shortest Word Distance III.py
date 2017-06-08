class Solution(object):
    def shortestWordDistance(self, words, word1, word2):
        """
        :type words: List[str]
        :type word1: str
        :type word2: str
        :rtype: int
        """
        p = q = -1
        distance = float('inf')
        for i in range(len(words)):
            if words[i] == word1:
                p = i
            if words[i] == word2:
                if word1 == word2:
                    p = q
                q = i
            if p!= -1 and q!= -1 and abs(p-q)<distance:
                distance = abs(p-q)
        return distance
