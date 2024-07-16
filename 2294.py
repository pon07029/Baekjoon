import sys
input = sys.stdin.readline
n,k = map(int, input().split())
li=[]
re=[999999] * (k+1)
for i in range(n):
    li.append(int(input()))
li=list(set(li))
li.sort()
tmp=0
for i in range(0,len(re),li[0]):
    re[i]=tmp
    tmp+=1
for i in range(1,len(li)):
    ad=li[i]
    for j in range(ad,len(re)):
        re[j]=min(re[j-ad]+1, re[j])
print(re[-1] if re[-1]<999999 else -1)