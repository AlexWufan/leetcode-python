class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.__list = [0] * size
        self.__window = size
        self.__count = 0

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        self.__count += 1
        self.__list[self.__count % self.__window] = val
        return sum(self.__list)/float(min(self.__count,self.__window))

##################### 上面这种最好。空间复杂度O(size)，时间复杂度O(1)############################

    def __init__(self, size):
        self.__list = []
        self.__window = size
        self.__count = 0

    def next(self, val):
        self.__count += 1
        self.__list.append(val)
        if self.__count < self.__window:
            return sum(self.__list[:self.__count])/float(self.__count)
        else:
            return sum(self.__list[self.__count-self.__window:self.__count])/float(self.__window)



# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)


# 下面使用deque，需要 import collections
    def __init__(self, size):
        self.queue = collections.deque(maxlen=size)
        

    def next(self, val):
        queue = self.queue
        queue.append(val)
        return float(sum(queue))/len(queue)


# 一行，stefen,q.append(v)会返回 False
class MovingAverage(object):
 def __init__(self, size):
  self.next = lambda v, q=collections.deque((), size): q.append(v) or 1.*sum(q)/len(q)