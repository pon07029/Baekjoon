m=1000000007
N=int(input())
li=list(map(int, input().split()))
ll=[1]*(N+1)
for i in range(1,N+1):
    ll[i]=ll[i-1]*2%m
li.sort()
def f(arr,l):
    if l==1:
        return 0,1,arr[0],arr[0],arr[0]
    c1,n1,s1,k1,j1=f(arr[:l//2],l//2)
    c2,n2,s2,k2,j2=f(arr[l//2:],l-l//2)
    c=((k2*(ll[n1]-1)-j1*(ll[n2]-1))+c1+c2)%m
    s=s1+s2
    k=(k1+k2*ll[n1])%m
    j=(j1*ll[n2]+j2)%m
    # print(c,n1+n2,s,k,j,"배열은 :", arr, (k2*(ll[n1]-1)-j1*(ll[n2]-1)))
    return c,n1+n2,s,k,j
print(f(li,N)[0])

        