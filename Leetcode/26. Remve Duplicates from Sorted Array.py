class Solution:
    def removeDuplicates(self, l) -> int:
        i=0
        while i+1<len(l):
            if l[i]==l[i+1]:
                l.remove(l[i])


            else:
                i+=1

        return len(l)