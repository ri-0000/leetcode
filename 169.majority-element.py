#
# @lc app=leetcode id=169 lang=python3
#
# [169] Majority Element
#

# @lc code=start
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result = dict()
        for i in nums:
            result[i] = result.get(i, 0)+1
        return max(result.items(), key=lambda x: x[1])[0]


# @lc code=end
