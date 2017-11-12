class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.max_ = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.max_ and x < self.max_[-1]:
            self.max_.append(self.max_[-1])
        else:
            self.max_.append(self.stack[-1])
    def pop(self):
        """
        :rtype: int
        """
        self.max_.pop()
        return self.stack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.max_[-1]

    def popMax(self):
        """
        :rtype: int
        """
        tmp = []
        m = self.max_[-1]
        while self.stack[-1] != m:
            tmp.append(self.pop())
        res = self.pop()
        while tmp:
            self.push(tmp.pop())
        return res

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()