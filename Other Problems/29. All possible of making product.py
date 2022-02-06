arr=[2,4,6,8]
pro=16

def solve(arr,pro):
    ans=[]
    all_per(arr,pro,0,ans,[])
    return ans
    
def all_per(arr,pro,index,ans,temp):
    if pro==1:
        x=temp[:]
        ans.append(x)
        return
    
    for i in range(index,len(arr)):
        if pro%arr[i]==0:
            temp.append(arr[i])
            all_per(arr,pro//arr[i],i,ans,temp)
            temp.remove(arr[i])
    
print(solve(arr,pro))