def caesarCipher(s, k):
    ci=""
    alpha="abcdefghijklmnopqrstuvwxyz"
    lalpha=set(alpha)
    ualpha=set(alpha.upper())
    for i in s:
        
        if i in lalpha:

            asci=ord(i)+k
            if asci>122:
                print(chr(95+(asci-122)),end="")
            else:
                print(chr(asci),end="")

        elif i in ualpha:
            asci=ord(i)+k
            if asci>90:
                print(chr(64+(asci-90)),end="")
            else:
                print(chr(asci),end="")

        else:
            print(i,end="")
            
       
        
    

caesarCipher("Hello_World!",4)