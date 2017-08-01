class Solution(object):
    def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        count = 0
        num = 0
        for i in range(len(abbr)):
            if abbr[i].isdigit():
                if abbr[i] == '0' and num == 0:
                    return False
                num = num*10 + int(abbr[i])
            else:
                count += num
                num = 0
                if count >= len(word) or word[count] != abbr[i] :
                    return False
                count += 1
        return num + count == len(word)