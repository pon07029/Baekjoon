a,b,c = map(int, input().split())
li=[[1,a%c]]
i=1
while i<b:
    i=li[-1][0]*2
    k =li[-1][1]**2%c
    li.append([i,k])
li.sort(reverse=True)
re =1
for i in li:
    if b>=i[0]:
        b-=i[0]
        re*=i[1]%c
print(re%c)