N, S =map(int, input().split())
li = list(map(int, input().split()))
su =[0]*(N+1)
start=-1

for i in range(1,N+1):
    su[i]=su[i-1]+li[i-1]

for i in range(N+1):
    if su[i]>=S:
        start=i
        break
l=start


for i in range(start,N+1):
    for j in range(i-l,i):
        if su[i]-su[j]>=S:
            l=i-j
        else:
            break
            

if start==-1:
    print(0)
    exit()

print(l)