class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.__stack = []
        self.__min = None
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.__stack:
            self.__min = x
        elif self.__min > x:
            self.__min = x
        self.__stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        pop = self.__stack.pop()
        if self.__min == pop:
            if self.__stack:
                self.__min = min(self.__stack)
            else:
                self.__min = None
        return pop

    def top(self):
        """
        :rtype: int
        """
        return self.__stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.__min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()