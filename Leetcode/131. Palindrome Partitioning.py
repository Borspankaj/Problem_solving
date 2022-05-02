class Solution:
    def partition(self, s: str) :
        idx = 0
        ans = []

        def backtrack(idx ,temp ,string ,ans , s):
            if idx == len(s):
                if len("".join(temp)) == len(s):
                    ans.append(temp[:])
                return
            string += s[idx]
            if string == string[::-1]:
                temp.append(string)
                st = string[:]
                string = ""             
                backtrack(idx + 1, temp, string, ans,s)
                string = st[:]
                temp.pop()


            backtrack(idx + 1,temp,string,ans,s)
            string = string[:-1]

        backtrack(idx,[],"",ans,s)
        return ans




            
