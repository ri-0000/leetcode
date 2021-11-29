#
# @lc app=leetcode id=46 lang=python3
#
# [46] Permutations
#

# @lc code=start
class Solution:
    def __init__(self) -> None:
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        self.length = len(nums)-1
        self.nums = nums
        self.gen()
        return self.result

    def gen(self,used=""):

        data = used.split(",")
        data.pop()
        data = [int(c) for c in data]

        if(self.length == len(data)-1):
            self.result.append(data)
            return

        
        for i in self.nums:
            if i in data:
                continue
            
            self.gen(used+str(i)+",")
            
        

        
        
        
# @lc code=end

