class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')

# better
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y

 The x & (x-1) trick makes sure it only iterates the fewest loop. Reusing x and y also improves a few ms in Python.