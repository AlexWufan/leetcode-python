class StringIterator(object):

    def __init__(self, compressedString):
        """
        :type compressedString: str
        """
        self.ch = " "
        self.num = 0
        self.index = 0
        self.s = compressedString

    def next(self):
        """
        :rtype: str
        """
        if not self.hasNext():
            return " "
        if not self.num:
            self.ch = self.s[self.index]
            self.index += 1
            while self.index < len(self.s) and self.s[self.index].isdigit():
                self.num = self.num*10 + int(self.s[self.index])
                self.index += 1
        self.num -= 1
        return self.ch
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.num > 0 or self.index < len(self.s)
        


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()