class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        str = str.strip()
        if str == '' : return 0
        flag = 1
        num = 0
        if str[0]=='-':
        	flag  = -1
        	str = str[1:]
        elif str[0]=='+':
        	str = str[1:]

        for i in range(len(str)):
            if i == 0 and str[i].isdigit()==False:
            	return 0
            elif str[i].isdigit():
            	digit = int(str[i])
            	num = 10*num + digit
            else : break 
        if num*flag > 2147483647:
        	return INT_MAX
        elif num*flag < -2147483648:
        	return INT_MIN
        return num*flag

if __name__=='__main__':
    asolution = Solution()
    print(asolution.myAtoi('-131231231231232312'))
