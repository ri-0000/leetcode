#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d = {'2':['a','b','c'],
        '3':['d','e','f'],
        '4':['g','h','i'],
        '5':['j','k','l'],
        '6':['m','n','o'],
        '7':['p','q','r','s'],
        '8':['t','u','v'],
        '9':['w','x','y','z'],}

        results = []

        for digit in digits:
            if len(results)==0:
                for c in d[digit]:
                    results.append(c)

            else:
                tmp = []
                for result in results:
                    for c in d[digit]:
                        tmp.append(result+c)
                results = tmp

        return results
            
            



        
        
# @lc code=end

