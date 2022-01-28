class Solution:
    def solve(self,ot,op,cl,ans):
        if op==0 and cl==0:
            ans.append(ot)
            return
        if op!=0 and op<cl:
            self.solve(ot+"(",op-1,cl,ans)
            self.solve(ot+")",op,cl-1,ans)
            
        else:
            if op==0:
                self.solve(ot+")",op,cl-1,ans)
            if op==cl:
                self.solve(ot+"(",op-1,cl,ans)
                
    def generateParenthesis(self, n: int):
        ans=[]
        self.solve("",n,n,ans)
        return ans