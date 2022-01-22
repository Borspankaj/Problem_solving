'''decimal = int(input(""))
binary = 0
ctr = 0
temp = decimal  


while(temp > 0):
    binary = ((temp%2)*(10**ctr)) + binary
    temp = int(temp/2)
    ctr += 1

binary.replace('1','*')
binary.replace('0','_')
binary.replace('*','0')
binary.replace('_','1')

print(binary)'''



def perfectCube(llist) :
    count=0
    for i in llist:
        cube = 0
        for val in range(i + 1) :
            cube = val**3
            if cube == N:
                count+=1
                break
            elif cube > N:
                break
    return count

if __name__ == "__main__" :
 
    N = 216
 
 
    perfectCube(N)