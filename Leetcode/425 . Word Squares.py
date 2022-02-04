class Solution:
    def wordSquares(self, words):
 

        def backtrack(row_no, temp_list, n):
            if len(temp_list)==n:
                x=temp_list[:]
                result.append(x)
                return
            prefix =""
            for word in temp_list:
                prefix+=word[row_no]
            pre_list=[]
            if prefix in hash_map:
                pre_list=hash_map[prefix]

            for word in pre_list:
                temp_list.append(word)
                backtrack(row_no+1, temp_list, n)
                temp_list.pop()
        result=[]
        hash_map=dict()
        for word in words:
            for i in range(len(word)-1):
                hash_map[word[:i+1]]=[]
        for word in words:
            for i in range(len(word)-1):
                hash_map[word[:i+1]].append(word)

        for i in range(len(words)):
            temp_list=[]
            temp_list.append(words[i])
            backtrack(1,temp_list,len(words[i]))
        return result