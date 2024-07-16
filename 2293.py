import sys
input = sys.stdin.readline
n,k = map(int, input().split())
li=[]
re=[0] * (k+1)
for i in range(n):
    li.append(int(input()))
li.sort()
for i in range(0,len(re),li[0]):
    re[i]=1
for i in range(1,len(li)):
    ad=li[i]
    for j in range(ad,len(re)):
        re[j]+=re[j-ad]
print(re[-1])