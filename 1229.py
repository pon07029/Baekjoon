N=int(input())
li=[1]
re=[6]*(N+1)
re[0]=1
for i in range(1,N):
    t=i*(i*2-1)
    if t>N: break
    li.append(t)

for i in li:
    re[i]=1

for i in li:
    for j in li:
        if i+j>N: break
        re[i+j]=min(2, re[i+j])

for i in range(1,N+1):
    for j in li:
        if i-j>=0:
            re[i]=min(re[i-j]+1, re[i])
            if re[i]<4: break
# print(*re)
print(re[-1])
