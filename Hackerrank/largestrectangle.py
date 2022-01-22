def solve(h):
    st=[]
    n=len(h)
    nser=[]
    nsel=[]
    for i in range(len(h)-1,-1,-1):
        while st and h[st[-1]]>=h[i]:
            st.pop()
        if not st:
            nser.append(-1)
        else:
            nser.append(st[-1])
        st.append(i)
    nser.reverse()
    st=[]
    for i in range(len(h)):
        while st and h[st[-1]]>=h[i]:
            st.pop()
        if not st:
            nsel.append(-1)
        else:
            nsel.append(st[-1])
        st.append(i)
    print(nsel)
    mr=0
    for i in range(n):
        rl=nsel[i]
        rr=nser[i] if nser[i]!=-1 else n 
        d=rr-rl-1
        m=d*h[i]
        mr=max(m,mr)
        
    return mr

