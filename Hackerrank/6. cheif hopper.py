arr=[2,3,4,3,2]
energy=0
for i in arr[::-1]:
    energy=(energy+i+1)//2

print(energy)
    
    
