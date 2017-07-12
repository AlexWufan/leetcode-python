class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = ['1']
        for i in range(2,n+1):
            num = res[i-2]
            tmp = ''
            count = 1
            for i in range(len(num)):
                if i+1 < len(num) and num[i] == num[i+1]:
                    count += 1
                elif i+1 < len(num) and num[i] != num[i+1]:
                    tmp += str(count) + num[i]
                    count = 1
                else:
                    tmp += str(count) + num[i]
            res.append(tmp)
        print(res)
        return res[-1]


if __name__ == '__main__':
    Asolution = Solution()
    print(Asolution.countAndSay(10))