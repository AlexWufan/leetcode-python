class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__dic = {}

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        # 这里不需要判断dic为空因为有默认返回值-1
        if self.__dic.get(message,-1) <= timestamp-10 or self.__dic.get(message,-1) == -1:
            self.__dic[message] = timestamp
            return True
        else:
            return False
            
            


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)