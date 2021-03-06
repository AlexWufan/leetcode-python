class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__set = []
        self.__pos = {}

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.__pos:
            return False
        else:
            self.__set.append(val)
            self.__pos[val] = len(self.__set)-1
            return True

    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.__pos:
            index = self.__pos[val]
            last = self.__set[-1]
            self.__set[index] = last
            self.__set.pop()
            self.__pos[last] = index
            self.__pos.pop(val)
            return True
        else:
            return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        # return self.__set[random.randint(0, len(self.__set)-1)]
        return random.choice(self.__set)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()