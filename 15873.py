p=input()
if len(p)==2:
    print(int(p[0])+int(p[1]))
elif len(p)==4:
    print(20)
else:
    if p[1]=='0':
        print(10+int(p[2]))
    else:
        print(int(p[0])+10)