#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        sum = 0
        tmp = 0
        for index in range(len(s)):
            if index+1 < len(s):
                current = s[index]
                next = s[index+1]
                current_index = order.index(current)
                next_index = order.index(next)
                if current_index < next_index:
                    sum -= map[current]+tmp
                    tmp = 0
                elif current_index == next_index:
                    tmp += map[current]
                else:
                    sum += map[current] + tmp
                    tmp = 0

            else:
                sum += map[s[index]]+tmp
                tmp = 0

            # print("sum", sum)

        return sum


# @lc code=end
