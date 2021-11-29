#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l = 0
        r = len(nums)-1
        while (l<=r):
            mid = (r+l)>>1

            if(nums[mid] == target):
                return mid 
            elif(nums[r]==target):
                return r
            
            if nums[l] < nums[mid]:
                if nums[l] <= target <=nums[mid]:
                    r =mid -1
                else:
                    l =mid+1
                
            else: 
                if nums[mid] <= target <=nums[r]:
                    l = mid +1
                else:
                    r = mid -1
                    
        return -1
    
        
        
# @lc code=end
