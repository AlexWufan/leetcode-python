class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__set = []
        self.__pos = collections.defaultdict(set)

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag =  val in self.__pos
        self.__set.append(val)
        self.__pos[val].add(len(self.__set)-1)
        return flag

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if self.__pos[val]:
            newval = self.__set[-1]
            i = self.__pos[val].pop()
            self.__set[i] = newval
            if self.__pos[newval]:
                self.__pos[newval].add(i)
                self.__pos[newval].discard(len(self.__set)-1)
            self.__set.pop()
            return True
        else:
            return False
        
    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return random.choice(self.__set)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()