class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        s = ' '.join(sentence) + ' '
        start = 0
        l = len(s)
        for i in range(rows):
            start += cols
            if s[start%l] == ' ':
                start += 1
            else:
                while s[(start-1)%l] != ' ':
                    start -= 1
            # print(start)
        return start/l