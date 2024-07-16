N = int(input())
li=list(map(int, input().split()))
li.sort()
if li[0]>=0:
    print(li[0], li[1])
    exit()
if li[-1]<=0:
    print(li[-2], li[-1])
    exit()
now= []
for i in range(N-1):
    if li[i]<=0 and li[i+1]>=0:
        now=[i, i+1]
        break
small=[abs(li[now[0]]+li[now[1]]),now[0],now[1] ]
i,j=now
while True:
    
    if i==0 and j==N-1:
        break
    if li[i]+li[j]<0:
        if j<N-1:
            j+=1
        else:
            i-=1
    elif li[i]+li[j]>0:
        if i>0:
            i-=1
        else:
            j+=1
    else:
        print(li[i], li[j])
        exit()
    if abs(li[i]+li[j])<small[0]:
        small=[abs(li[i]+li[j]),i,j]

print(li[small[1]], li[small[2]])
