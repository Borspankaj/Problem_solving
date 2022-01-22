s=input()
op=[]
while True:
    if '0' not in s:
        print('NO')
        
    elif s.count('1')==1:
        op.append([2,s.find('1')])
        s.replace('1','0')
    
        


