class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        m = 0
        for i in range(32):
            m <<= 1
            m += n & 1
            n >>= 1
        return m