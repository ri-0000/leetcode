#
# @lc app=leetcode id=1160 lang=python3
#
# [1160] Find Words That Can Be Formed by Characters
#

# @lc code=start
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        result = 0

        d = dict()
        for c in chars:
            d[c] = d.get(c,0)+1
        
        for word in words:
            for c in word:
                if(word.count(c)> d.get(c,0)):
                    break
            else:
                result += len(word)
        return result
            
        
# @lc code=end

