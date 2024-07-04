a, b= map(str, input().split())
c=[]
d=[]
for i in range(len(a), 0, -1):
    c.append(int(a[i-1]))
for i in range(len(b), 0, -1):
    d.append(int(b[i-1]))
c =''.join(map(str, c))
d =''.join(map(str, d))
print(max(int(c), int(d)))