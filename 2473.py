N=int(input())
li=list(map(int, input().split()))
li.sort()
re=[]
mn=9999999999999
for i in range(N-2):
    for j in range(i+1,N-1):
        s,e=j+1,N
        mid=(s+e)//2
        while s<e:
            tot=li[i]+li[j]+li[mid]
            if abs(tot)<mn:
                mn=abs(tot)
                re=[li[i],li[j],li[mid]]
            if tot<0: s=mid+1
            else: e=mid
            mid=(s+e)//2
print(*re)
