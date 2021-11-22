#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            num = nums[i]
            add = target - num
            if add in hash_table.keys():
                return [hash_table[add], i]
            else:
                hash_table[num] = i

        # @lc code=end
