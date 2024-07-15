N = int(input())
li=[1]
p=2
re=[i for i in range(N+1)]
while True:
    li.append(li[-1]+p*(p+1)//2)
    p+=1
    if li[-1]>N:
        break
for i in range(1,N+1):
    for j in li:
        if i<j:
            break
        re[i]=min(re[i],re[i-j]+1)
print(re[-1])