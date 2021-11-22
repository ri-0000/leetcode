#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        table = set()

        while True:
            n = str(n)
            sum = 0
            for c in n:
                i = int(c)
                sum += i*i
            if sum in table:
                return False
            elif sum == 1:
                return True
            table.add(sum)
            n = sum


# @lc code=end
