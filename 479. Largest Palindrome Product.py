class Solution(object):
    def largestPalindrome(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 9
        upper = 10**n - 1
        lower = 10**(n-1)
        for i in range(upper, lower-1, -1):
            palindrome = int(str(i)+str(i)[::-1])
            for j in range(upper, lower - 1, -1):
                if palindrome //j > upper:
                    break
                elif palindrome % j == 0: #and lower <= palindrome // j <= upper:
                    return palindrome % 1337
        return False
        