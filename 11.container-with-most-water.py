#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        result = -1
        l,r = 0,len(height)-1
        while(l-r!=0):
            if (height[r]>height[l]):
                result = max(result,height[l]*(r-l))
                l+=1
            else:
                result = max(result,height[r]*(r-l))
                r-=1
        return result
                
                

                
                


        
# @lc code=end