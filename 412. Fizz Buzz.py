class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 想到的另一种写法
        output = [str(x) for x in range(1,n+1)]
        output[2::3] = ['Fizz'] * (n // 3)
        output[4::5] = ['Buzz'] * (n // 5)
        output[14::15] = ['FizzBuzz'] * (n // 15)

        # 一般方法
        # for x in range(1,n+1):
        # 	if x % 3 ==0 and x % 5 == 0:
        # 		output.append('FizzBuzz')
        # 	elif x % 3 == 0:
        # 		output.append('Fizz')
        # 	elif x % 5 == 0:
        # 		output.append('Buzz')
        # 	else:
        # 		output.append(str(x))
        return output

if __name__=='__main__':
	aSolution = Solution()
	print(aSolution.fizzBuzz(15))

