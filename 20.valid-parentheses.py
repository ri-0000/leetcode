#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        open = ["(", "[", "{"]
        close = [")", "]", "}"]
        valid = ["()", "[]", "{}"]
        stack = list()
        for c in s:
            if len(stack)-1 >= 0:
                top = stack[len(stack)-1]
                if top in open and c in close:
                    if top+c not in valid:
                        print()
                        return False

                if top+c in valid:
                    stack.pop()
                else:
                    stack.append(c)
            else:
                stack.append(c)
        return len(stack) == 0


# @lc code=end
