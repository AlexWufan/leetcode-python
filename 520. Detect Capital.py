class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        return word == word.capitalize() or word == word.upper() or word ==word.lower()
        # return word.isupper() or word.islower() or word.istitle()