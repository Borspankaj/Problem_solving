class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        brc={'(':')','{':'}','[':']'}
        
        for b in s:
            if b in '{[(':
                stack.append(b)
                
            else:
                
                if stack:
                
                    top=stack.pop()
                    if brc[top]!=b:
                        return False
                else:
                    return False
                
        return False if stack else True