# LEETCODE PROBLEM 380 : INSERT DELETE GETRANDOM O(1)
# https://leetcode.com/problems/insert-delete-getrandom-o1/description/
import random
class RandomizedSet(object):

    def __init__(self):
        self.set = set()
        self.map = {}
        self.items = []

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            return False
        self.set.add(val)
        self.items.append(val)
        self.map[val] = len(self.items) - 1
        return True
        

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.set:
            self.set.remove(val)
            self.items[self.map[val]] = 'empty'
            return True
        return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        print(self.set)
        print(self.map)
        print(self.items)
        index = random.randint(0, len(self.items) - 1)
        while self.items[index] == 'empty':
            index = random.randint(0, len(self.items) - 1)
        return self.items[index]
        

obj = RandomizedSet()
print(obj.insert(1))
print(obj.remove(2))
print(obj.insert(2))
print(obj.getRandom())