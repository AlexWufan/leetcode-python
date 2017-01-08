class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res, index = self.dfs(s, 0)
        return res



    def dfs(self, s, index):
    	res = ''
    	num = ''
    	while index < len(s):
    		if s[index].isdigit:
    			num += s[index]
    		elif s[index] == '[':
    			tmp, j = self.dfs(s, index+1)
    			res += tmp
    			num = ''
    		elif s[index] == ']':
    			index += 1
    			return res, index
    		else: res+= s[index]

    	return (res, index)

#上面是递归，没写出来。每遇到'['启动一个dfs
#下面是迭代，用栈。
	def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [['', 1]]
        num = ''
        for ch in s:
        	if ch.isdigit():
        		num += ch
        	elif ch == '[':
        		stack.append(['', int(num)])
        		num = ''
        	elif ch == ']':
        		string, k = stack.pop()
        		stack[-1][0] += string*k
        	else:
        		stack[-1][0] += ch
        return stack[-1][0]

# 用两个栈，比较一般的写法,注意后面索引都是-1
class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        num = ''
        numstack = [1]
        strstack = ['']
        for ch in s:
        	if ch.isdigit():
        		num += ch
        	elif ch == '[':
        		numstack.append(int(num))
        		num = ''
        		strstack.append('')
        	elif ch == ']':
        		string = strstack.pop()
        		k = numstack.pop()
        		strstack[-1] += string * k
        	else:
        		strstack[-1] += ch
        return strstack[0]