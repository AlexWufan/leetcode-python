class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3: return 0
        p = [1] * n
        p[0]=p[1]=0
        for i in range(2, int(n**0.5)+1):
        	if p[i]:
        		p[i*i:n:i] = [0] * len(range(i*i, n, i))
        return sum(p)







        # def isPrime(n):
        # 	if n <= 1: return False
        # 	for x in range(2, int(n**0.5)+1):
        # 		if n%x == 0:
        # 			return False
        # 	return True

        # for x in range(2,n):
        # 	if isPrime(x):
        # 		num += 1
        # return num

if __name__ == '__main__':
	aSolution = Solution()
	print(aSolution.countPrimes(3))

# class Solution:
# # @param {integer} n
# # @return {integer}
# def countPrimes(self, n):
#     if n < 3:
#         return 0
#     primes = [True] * n
#     primes[0] = primes[1] = False
#     for i in range(2, int(n ** 0.5) + 1):
#         if primes[i]:
#             primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
#     return sum(primes)