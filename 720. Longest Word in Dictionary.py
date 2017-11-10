class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words)
        A = set()
        res = ''
        for word in words:
            if len(word) == 1 or word[:-1] in A:
                A.add(word)
                if len(word) > len(res):
                    res = word 
        return res