class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        dic = {4:'M', 3.5:'D', 3:'C', 2.5:'L', 2:'X', 1.5:'V', 1:'I'}
        l = len(str(num))
        roman = ''
        for i in range(l):
            if int(str(num)[i]) <= 3: 
                roman += dic[l-i] * int(str(num)[i])   
            elif int(str(num)[i]) == 4: 
                roman += dic[l-i] + dic[ l-i + 0.5]
            elif int(str(num)[i]) == 9:
                roman += dic[l-i] + dic[l-i+1]
            else:
                roman += dic[ l-i + 0.5] + dic[l-i] * (int(str(num)[i])-5)
        return roman

if __name__=='__main__':
    asolution = Solution()
    print(asolution.intToRoman(99))