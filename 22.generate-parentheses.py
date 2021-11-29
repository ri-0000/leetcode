#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start

class Solution:
    def __init__(self) -> None:
        self.result =[]
        self.end = 0

    def generateParenthesis(self, n: int) -> List[str]:
        self.end = n*2
        self._gen(2*n)
        return self.result

    def _gen(self,n,string=""):

        if n == 0:
            if self.check(string,True):
                self.result.append(string)
            return 

        chars = ["(",")"]
        for c in chars:
            if(self.check(string+c)):
                
                self._gen(n-1,string+c)
            else:
                pass
                

    def check(self,s:str,flag=False)-> bool:
        tmp = ""

        for c in s :
            tmp+=c

            if(tmp[0]==")"):
                return False

            if(tmp.endswith("()")):
                tmp = tmp[0:-2]

        if flag :
            return len(tmp) ==0
        else:
            return len(tmp) ==0 or (tmp.count("(")==len(tmp) and tmp.count("(")<=self.end//2)
    
        
    
    
    

        
# @lc code=end


