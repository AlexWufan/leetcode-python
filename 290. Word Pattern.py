class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        p = [0 for x in pattern]
        flag = 0
        set1 = set(pattern)
        for i in range(len(pattern)):
        	if pattern[i] in set1:
        		flag += 1
        		set1.remove(pattern[i])
        	else: pass
        	for j in range(len(pattern)):
        		if pattern[i] == pattern[j] and p[j] == 0:
        			p[j] = flag

        flag = 0
        str = list(str.split( ))
        s = [0 for x in str]
        set2 = set(str)

        for i in range(len(str)):
        	if str[i] in set2:
        		flag += 1
        		set2.remove(str[i])
        	else: pass
        	for j in range(len(str)):
        		if str[i] == str[j] and s[j] == 0:
        			s[j] = flag

        return True if s == p else False

if __name__=='__main__':
    asolution = Solution()
    print(asolution.wordPattern('abbaaabccab', 'dog cat dog'))

#better solution
# def wordPattern(self, pattern, str):
#     s = pattern
#     t = str.split()
#     return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)