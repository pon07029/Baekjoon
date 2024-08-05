
def f(n,k):
    if n==1:
        arr=[1 for _ in range(k+1)]
        arr[0]=0
        return arr
    dp = f(n-1,k)
    su=sum(dp)
    li=[su]*(k+1)
    li[0]=0
    for i in range(1,k+1):
        for j in range(2*i,k+1,i):
            li[j]-=dp[i]
    for i in range(1,k+1):
        li[i]%=(10**9+7)
    return li
a,b=map(int,input().split())
print(sum(f(a,b))%(10**9+7))