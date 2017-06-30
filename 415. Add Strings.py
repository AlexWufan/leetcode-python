class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l1 = len(num1)-1
        l2 = len(num2)-1
        carry = 0
        res = ''
        while l1 >= 0 or l2 >= 0 or carry:
            x = num1[l1] if l1 >= 0 else '0'
            y = num2[l2] if l2 >= 0 else '0'
            temp = ord(x)-ord('0') + ord(y) - ord('0') + carry
            res += str(temp%10)
            carry = temp//10
            l1-=1
            l2-=1
        return res[::-1]

if __name__ == '__main__':
    Asolution = Solution()
    print(Asolution.addStrings('1','9'))
