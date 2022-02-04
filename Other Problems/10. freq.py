n=input()
l=i=0
d={}
temp=""
while i<len(n):
    if n[i]==" ":
        if temp in d:
            d[temp][0]+=1
            d[temp][1]=l
        else:
            d[temp]=1
            d[temp][1]=l
    else:
        temp+=n[i]
        l+=1