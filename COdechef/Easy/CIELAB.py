try:
    
    v = list(map(int,input().split()))
    a,b = v[0] , v[1]

    
    val = max(a,b) - min(a,b)

    if val%10!=9 :
        print (val+1)

    else :
        print (val-1)
   

except Exception as e : 

    pass
        