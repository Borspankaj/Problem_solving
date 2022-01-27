s='123'
su=prev=0
for i in range(len(s)):
    prev=(i+1)*int(s[i])+ (10*prev)
    su+=prev
print(su%(10**9+7))

