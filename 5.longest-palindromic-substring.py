#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        size = len(s)
        result = s[0]
        for i in range(1, size-1):
            first_half = s[0, i]
            latter_half = s[i, i*2]
            if first_half == latter_half:
                result = first_half + latter_half
        return result

# @lc code=end
