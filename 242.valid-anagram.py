#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        d1 = dict()
        d2 = dict()
        for c in s:
            d1[c] = d1.get(c, 0)+1

        for c in t:
            d2[c] = d2.get(c, 0)+1

        return d1 == d2

# @lc code=end
