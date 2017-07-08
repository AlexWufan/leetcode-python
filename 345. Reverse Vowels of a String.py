class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        p, q = 0, len(s)-1
        s_list = list(s)
        vowels = 'aeiouAEIOU'

        while p<q:
            if s_list[p] in vowels and s_list[q] in vowels:
                s_list[p], s_list[q] = s_list[q], s_list[p]
                p += 1
                q -= 1
            elif s_list[p] not in vowels:
                p += 1
            elif s_list[q] not in vowels:
                q -= 1
        return ''.join(s_list)