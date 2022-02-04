s='asdf'

d={'a':1,'b':1,'c':2,'d':2,'e':2,'f':3,'g':3,'h':3,'i':4,'j':4,'k':4,'l':5,'m':5,'n':5,'o':6,'p':6,'q':6,'r':7,'s':7,'t':7,'u':8,'v':8,'w':8,'x':9,'y':9,'z':9}



count=0
for i in range(len(s)):

    for j in range(len(s)):
        summ=0
        l=0
        for k in range(i,j+1):
            summ+=d[s[k]]
            l+=1
          
        if l!=0 and summ%l==0:
            count+=1
        
print(count)