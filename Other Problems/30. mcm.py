


def rmcm(arr,i,j,dp):
    if i==j:
        dp[i][j]=0

    if dp[i][j]!=-1:
        return dp[i][j]
    mini=1000000
    for k in range(i,j):
        count=rmcm(arr,i,k,dp) + rmcm(arr,k+1,j,dp) + arr[i-1] * arr[k] * arr[j]
        if count<mini:
            mini=count
    dp[i][j]=mini

    return dp[i][j]

def mcm(arr,n):
    dp=[[-1] * n for i in range(n)]
    return rmcm(arr,1,n-1,dp)

arr=[2,3,4,3,5]
ans=mcm(arr,5)
print(ans)