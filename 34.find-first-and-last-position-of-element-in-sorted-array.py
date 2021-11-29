#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index =self.bin_search(nums,target)
        r = index
        l = index
        
        
        if (index == -1):
            return -1 , -1
        else:
            while(0<= l and nums[l] ==target):
                l -=1
                
            while(len(nums)-1 >=r and nums[r] == target):
                r +=1
        return [l+1,r-1]
            
            

            
        
        
    def bin_search(self,nums:List[int],target:int)-> int:
        r = len(nums)-1
        l = 0
        while (l<=r):
            mid = (r+l)>>1

            if (nums[mid]== target):
                return mid
            if(nums[mid]<target):
                l =mid +1
            else:
                r = mid -1
        return -1
        
# @lc code=end

