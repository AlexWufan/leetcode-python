class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        b = {value:index for index, value in enumerate(B)}
        return [b[x] for x in A]
        