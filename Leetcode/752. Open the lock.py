class Solution:
    def openLock(self, deadends, target) :
        q=[]
        visited=set()
        for ends in deadends:
            visited.add(ends)
        l="0000"
        if l in visited:
            return -1

        q.append((0,l))
        visited.add(l)

        while q:
            dis,state=q.pop(0)
            if state==target:
                return dis
            copy=list(state)

            for i in range(4):
                c1=copy[:]
                c2=copy[:]
                c1[i]=str((int(c1[i])+1)%10)
                c1="".join(c1)
                c2[i]=str((int(c2[i])-1)%10)
                c2="".join(c2)
                if c1 not in visited:
                    visited.add(c1)
                    q.append((dis+1,c1))


                if c2 not in visited:
                    visited.add(c2)
                    q.append((dis+1,c2))


        return -1

