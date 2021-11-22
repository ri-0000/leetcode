#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        if(m == 0):
            for i in range(n):
                nums1[i] = nums2[i]
            return
        elif (n == 0):
            return

        point = n+m - 1
        m -= 1
        n -= 1

        while(n >= 0 and m >= 0):
            if(nums1[m] > nums2[n]):
                nums1[point] = nums1[m]
                m -= 1
            else:
                nums1[point] = nums2[n]
                n -= 1
            point -= 1

        if(m < 0):
            while(n >= 0):
                nums1[point] = nums2[n]
                n -= 1
                point -= 1


# @lc code=end
