class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        a = (C-A)*(D-B)
        b = (G-E)*(H-F)
        c = max((min(C, G)-max(E,A)), 0)*max((min(H,D)-max(B,F)), 0)
        return a+b-c