# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         for x in ransomNote:
#         	if ransomNote.count(x) > magazine.count(x):
#         		return False
#         return True

# 这种写法很慢，换一个
import collections
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        return not collections.Counter(ransomNote) - collections.Counter(magazine)

if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.canConstruct('aa','aab'))

# 或者 来自leetcode discuss, 最快
def canConstruct(self, ransomNote, magazine):
    return all(ransomNote.count(i) <= magazine.count(i) for i in string.ascii_lowercase)