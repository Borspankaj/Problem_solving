class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        visited=set()
        q=[]
        words=set(wordList)
        
        q.append((1,beginWord))
        if beginWord in words:
            words.remove(beginWord)
        
        while q:
            step,c=q.pop(0)
            if c==endWord:
                return step
            
            for i in range(len(c)):
                curr=list(c)
                for j in range(26):
                    curr[i]=chr(97+j)
                    new="".join(curr)
                    if new in words:
                        q.append((step+1,new))
                        words.remove(new)
                        
        return 0