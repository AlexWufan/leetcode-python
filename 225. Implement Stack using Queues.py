class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inque = []
        self.outque = []
        self.top_value = None

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: void
        """
        self.inque.append(x)
        self.top_value = x

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        for i in range(len(self.inque)-1):
            self.top_value = self.inque.pop(0)
            self.outque.append(self.top_value)
            
        self.inque, self.outque = self.outque, self.inque
        return self.outque.pop(0)
            

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        return self.top_value

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.inque and not self.outque
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()