#
# @lc app=leetcode id=705 lang=python3
#
# [705] Design HashSet
#

# @lc code=start
class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.size = 1000
        self.table = [None] * self.size

    def add(self, key: int) -> None:
        index = key % self.size
        if self.table[index] is None:
            self.table[index] = [key]
        else:
            self.table[index].append(key)

    def remove(self, key: int) -> None:

        index = key % self.size
        node = self.table[index]
        if node is None:
            return
        self.table[index] = [i for i in self.table[index] if i != key]

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """

        index = key % self.size
        node = self.table[index]
        if node is None:
            return False
        for i in node:
            if i == key:
                return True
        else:
            return False

# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
# @lc code=end
