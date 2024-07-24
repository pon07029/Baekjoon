import sys
input=sys.stdin.readline
n=int(input())
a=[0]*n
b=[0]*n
c=[0]*n
d=[0]*n
a1=[]
b1=[]
result=0
for i in range(n):
    a[i],b[i],c[i],d[i]=map(int,input().split())

for i in range(n):
    for j in range(n):
        a1.append(a[i]+b[j])
        b1.append(c[i]+d[j])
a1.sort()
b1.sort()
start=0
end=n*n-1
while start<n*n and end>=0:
    if a1[start]+b1[end]==0:
        a1_count=1
        b1_count=1
        start+=1
        end-=1
        while start<n*n and a1[start]==a1[start-1]:
            a1_count+=1
            start+=1
        while end>=0 and b1[end]==b1[end+1]:
            b1_count+=1
            end-=1
        result+=a1_count*b1_count
    elif a1[start]+b1[end]>0:
        end-=1
    else:
        start+=1
print(result)