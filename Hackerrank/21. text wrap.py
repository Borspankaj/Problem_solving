s="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
k=4
new=""
for i in range(0,len(s),k):
    new+=s[i:i+k]+"\n"

print(new)


