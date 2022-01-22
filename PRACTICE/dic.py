d={1:2,
    7:3,
    6:4,
    4:5}

for i in sorted(d.items()):
    print(i)
print(d)

'''print(d.items())
print(d.values())
print(d.keys())
print(sorted(d.items()))
'''
d[1]='GG'
print(d)


d.update({1:'FF'})

print(d)


print(d[int(input())])

