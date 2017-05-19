class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return len(candies)/2 if (len(set(candies)) > len(candies)/2) else len(set(candies))