class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        reverse = ''
        hashmap = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
        for x in num:
            if x in hashmap:
                reverse = hashmap[x] + reverse
            else:
                return False
        return reverse == num