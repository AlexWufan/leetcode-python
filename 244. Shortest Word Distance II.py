class WordDistance(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.dict = {}
        for i, word in enumerate(words):
            self.dict[word] = self.dict.get(word, []) + [i]

    def shortest(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        index1, index2 = self.dict[word1], self.dict[word2]
        i, j ,distance = 0, 0, float('inf')
        while i < len(index1) and j < len(index2):
            distance = min(abs(index1[i] - index2[j]), distance)
            if index1[i] < index2[j]:
                i+=1
            else:
                j+=1
        return distance


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(words)
# param_1 = obj.shortest(word1,word2)